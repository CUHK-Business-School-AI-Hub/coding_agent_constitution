"""Regression tests for the public lint command; Python standard library only."""

from pathlib import Path
import re
import subprocess
import tempfile
import unittest
from urllib.parse import unquote, urlsplit


SCRIPT = Path(__file__).with_name("check-governance.sh")
EXAMPLE = SCRIPT.parent.parent / "assets/examples/feedback-inbox"
TASK = """# Task: Check a result
## Goal
Check one result.
## Source Context
- docs/PLAN.md
## Scope
- Touch: result.txt
- Do not touch: other files
## Interfaces
- Consumes: None
- Produces: result.txt
- Public contracts touched: None
- Downstream tasks relying on this: None
## Acceptance Criteria
- The result matches the expected value.
## Verification
- Command: test -f result.txt
  - Expected evidence: exit 0
## Governance Drift Check
- No public behavior changes.
"""


class GovernanceLintTests(unittest.TestCase):
    def run_lint(self, task=None, files=None, mode=None):
        with tempfile.TemporaryDirectory(prefix="constitution-test-") as tmp:
            root = Path(tmp)
            inputs = dict(files or {})
            if task is not None:
                inputs["docs/TASKS/001-task.md"] = task
            for name, content in inputs.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content.encode())
            return subprocess.run(
                ["bash", str(SCRIPT)] + (["--mode", mode] if mode else []) + [str(root)],
                text=True, capture_output=True
            )

    def assert_rejected(self, task, reason):
        result = self.run_lint(task)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(reason, result.stdout)

    def test_complete_task(self):
        result = self.run_lint(TASK)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("ERROR", result.stdout)

    def test_each_required_heading_is_required(self):
        for heading in ("Goal", "Source Context", "Scope", "Interfaces",
                        "Acceptance Criteria", "Verification", "Governance Drift Check"):
            with self.subTest(heading=heading):
                self.assert_rejected(TASK.replace("## " + heading, heading), "missing sections")

    def test_body_keywords_do_not_replace_headings(self):
        task = "# Task\n## Goal\nSource\nContext\nScope\nAcceptance\nCriteria\nVerification\nGovernance\nDrift\nCheck\n## Interfaces\n- Consumes: None\n- Command: true\n"
        self.assert_rejected(task, "missing sections")

    def test_fenced_example_does_not_supply_missing_section(self):
        for fence in ("```", "~~~", "````"):
            with self.subTest(fence=fence):
                task = TASK.replace("## Verification", "Verification")
                task += f"\n{fence}markdown\n## Verification\n- Command: true\n- Expected evidence: exit 0\n{fence}\n"
                self.assert_rejected(task, "missing sections")

    def test_command_must_be_in_verification(self):
        task = TASK.replace("- Command: test -f result.txt", "No command supplied.")
        task = task.replace("## Goal", "## Goal\n- Command: true")
        self.assert_rejected(task, "exact non-empty command")

    def test_evidence_must_be_in_verification(self):
        task = TASK.replace("  - Expected evidence: exit 0", "")
        task += "\n- Expected evidence: exit 0\n"
        self.assert_rejected(task, "Expected evidence")

    def test_empty_command_and_evidence_are_rejected(self):
        for old, new, reason in (
            ("Command: test -f result.txt", "Command: ", "command"),
            ("Command: test -f result.txt", "Command: ``", "command"),
            ("Expected evidence: exit 0", "Expected evidence: ", "Expected evidence"),
        ):
            with self.subTest(new=new):
                self.assert_rejected(TASK.replace(old, new), reason)

    def test_interface_fields_cannot_be_supplied_elsewhere(self):
        for field in ("Consumes: None", "Produces: result.txt", "Public contracts touched: None",
                      "Downstream tasks relying on this: None"):
            with self.subTest(field=field):
                self.assert_rejected(TASK.replace("- " + field, "") + "\n- " + field, "Interfaces should include")

    def test_open_questions_can_remain_unresolved(self):
        result = self.run_lint(TASK + "\n## Open Questions\n- TODO: choose a region before deployment.\n")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_placeholder_outside_open_questions_is_rejected(self):
        self.assert_rejected(TASK + "\n## Open Questions\n- TODO: choose region.\n## Risks\n- TODO: define risk.\n", "placeholder")

    def test_code_example_cannot_open_questions_exemption(self):
        self.assert_rejected(TASK + "\n```markdown\n## Open Questions\n```\n- TODO: unfinished requirement.\n", "placeholder")

    def test_unfinished_contract_example_is_rejected(self):
        self.assert_rejected(TASK + '\n```json\n{"value": "TODO"}\n```\n', "placeholder")

    def test_crlf_and_trailing_spaces(self):
        result = self.run_lint(TASK.replace("\n", "  \r\n"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_empty_scan_is_explicit(self):
        result = self.run_lint()
        self.assertEqual(result.returncode, 0)
        self.assertIn("No governance files found", result.stdout)
        self.assertNotIn("checks passed", result.stdout)

    def test_flexible_briefs_are_explicitly_outside_lint_coverage(self):
        for path in ("docs/PLAN.md", "PLAN.md", "docs/BRIEF.md", "BRIEF.md"):
            with self.subTest(path=path):
                result = self.run_lint(files={path: "# Brief\n"})
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("not structurally checked", result.stdout)
                self.assertNotIn("checks passed", result.stdout)

    def test_explicit_standard_retains_default_validation(self):
        invalid = TASK.replace("## Interfaces", "Interfaces")
        default = self.run_lint(invalid)
        explicit = self.run_lint(invalid, mode="standard")
        self.assertEqual(default.returncode, 1)
        self.assertEqual(explicit.returncode, default.returncode)
        self.assertEqual(explicit.stdout, default.stdout)

    def test_flash_does_not_require_standard_sections_or_commands(self):
        result = self.run_lint(
            task="# Memo edit\nShorten supplied memo; compare figures and inspect rendering.\n",
            files={"docs/ARCH.md": "# Existing context\nUse the existing document template.\n"},
            mode="flash",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("missing sections", result.stdout)
        self.assertNotIn("exact non-empty command", result.stdout)
        self.assertNotIn("Product Shape", result.stdout)
        self.assertIn("Standard document-section checks were not run", result.stdout)
        self.assertNotIn("checks passed", result.stdout)

    def test_flash_keeps_free_form_unknowns_without_standard_headings(self):
        brief = "# Research brief\n## Outcome\nCompare supplied options.\n## Unknowns\n- TODO: confirm delivery date before a dated recommendation.\n"
        result = self.run_lint(task=brief, mode="flash")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("placeholder", result.stdout)
        self.assertIn("task-specific review", result.stdout)

    def test_flash_keeps_shared_adapter_findings(self):
        result = self.run_lint(files={"CLAUDE.md": "@AGENTS.md\n"}, mode="flash")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("AGENTS.md is missing", result.stdout)
        self.assertIn("task-specific review", result.stdout)

    def test_flash_does_not_claim_conversation_contract_was_checked(self):
        result = self.run_lint(mode="flash")
        self.assertEqual(result.returncode, 0)
        self.assertIn("No governance files found", result.stdout)
        self.assertIn("task-specific review", result.stdout)
        self.assertNotIn("checks passed", result.stdout)

    def test_invalid_cli_mode_and_extra_arguments_are_rejected(self):
        for args in (("--mode",), ("--mode", "other"), ("--unknown",), (".", ".")):
            with self.subTest(args=args):
                result = subprocess.run(["bash", str(SCRIPT), *args], text=True, capture_output=True)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_native_agents_needs_no_claude_adapter(self):
        result = self.run_lint(files={"AGENTS.md": "# Shared instructions\n"})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("WARN", result.stdout)

    def test_claude_entries_without_canonical_file_are_orphans(self):
        for entry in ("CLAUDE.md", ".claude/CLAUDE.md", "CLAUDE.local.md"):
            with self.subTest(entry=entry):
                result = self.run_lint(files={entry: "# Project instructions\n"})
                self.assertEqual(result.returncode, 1, result.stdout)
                self.assertIn("AGENTS.md is missing", result.stdout)

    def test_shadowing_entries_without_import_warn(self):
        for entry in ("CLAUDE.md", ".claude/CLAUDE.md", "CLAUDE.local.md"):
            with self.subTest(entry=entry):
                result = self.run_lint(files={"AGENTS.md": "# Shared\n", entry: "Read AGENTS.md.\n"})
                self.assertEqual(result.returncode, 0, result.stdout)
                self.assertIn("can suppress native", result.stdout)

    def test_supported_thin_imports_do_not_warn(self):
        for entry, content in (("CLAUDE.md", "@AGENTS.md\n"),
                               ("CLAUDE.md", "@./AGENTS.md  \r\n"),
                               (".claude/CLAUDE.md", "@../AGENTS.md\n"),
                               ("CLAUDE.local.md", "@AGENTS.md\n")):
            with self.subTest(entry=entry, content=content):
                result = self.run_lint(files={"AGENTS.md": "# Shared\n", entry: content})
                self.assertEqual(result.returncode, 0, result.stdout)
                self.assertNotIn("can suppress native", result.stdout)

    def test_import_examples_do_not_hide_shadowing(self):
        for content in ("```markdown\n@AGENTS.md\n```\n", "Use `@AGENTS.md`.\n", "@OTHER-AGENTS.md\n"):
            with self.subTest(content=content):
                result = self.run_lint(files={"AGENTS.md": "# Shared\n", "CLAUDE.md": content})
                self.assertIn("can suppress native", result.stdout)

    def test_claude_rules_alone_do_not_suppress_native_discovery(self):
        result = self.run_lint(files={"AGENTS.md": "# Shared\n", ".claude/rules/style.md": "# Local style\n"})
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn("can suppress native", result.stdout)

    def test_bundled_example_remains_compatible(self):
        result = subprocess.run(["bash", str(SCRIPT), str(EXAMPLE)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("ERROR", result.stdout)


class ShippedInstructionContractTests(unittest.TestCase):
    """Static asset consistency checks, not model-behavior evaluations."""

    root = SCRIPT.parent.parent

    def read(self, path):
        return (self.root / path).read_text()

    def test_astra_routing_and_authorization_are_preserved(self):
        skill = self.read("SKILL.md")
        for phrase in ("Skip already-scoped code changes", "planning, produce the requested documents and stop",
                       "Do not load every document", "there is no minimum count",
                       "do not ask again for the same decision", "Fix findings introduced by this change"):
            self.assertIn(phrase, skill)

    def test_example_and_template_keep_portable_execution_boundaries(self):
        for path in ("assets/governance-templates/AGENTS.md", "assets/examples/feedback-inbox/AGENTS.md"):
            with self.subTest(path=path):
                content = self.read(path)
                for phrase in ("planning-only", "explicitly approved task", "production deployment",
                               "background work", "blocked/pending", "do not grant authority"):
                    self.assertIn(phrase.lower(), content.lower())
                self.assertNotIn("stop and split", content)
                self.assertNotIn("Always read", content)
                self.assertNotIn("What Cursor should review", content)

    def test_example_has_one_canonical_entry(self):
        self.assertTrue((EXAMPLE / "AGENTS.md").exists())
        for path in ("CLAUDE.md", ".claude/rules/project-governance.md", ".cursor/rules/project-governance.mdc"):
            self.assertFalse((EXAMPLE / path).exists(), path)
        self.assertTrue(self.read("assets/governance-templates/CLAUDE.md").startswith("@AGENTS.md\n"))

    def test_flash_routes_away_from_standard_bootstrap(self):
        skill = self.read("SKILL.md")
        flash = self.read("references/flash-mode.md")
        self.assertIn("go directly to `references/flash-mode.md`", skill)
        self.assertIn("not its bootstrap sequence", skill)
        self.assertIn("## Workflow (Standard And Retrofit)", skill)
        self.assertIn("A clear small task can proceed directly", flash)
        self.assertIn("planning-only", flash)
        self.assertIn("blocked or pending state", flash)

    def test_flash_common_contract_and_revisable_plan(self):
        flash = self.read("references/flash-mode.md")
        for label in ("Goal", "User or audience", "Context", "Scope", "Constraints",
                      "Observable completion", "Unknowns"):
            self.assertIn("**" + label + ":**", flash)
        for phrase in ("Outcome Versus Implementation Plan", "in the conversation",
                       "not an exact file set", "rather than reproducing them",
                       "not four exclusive modes or four compulsory files"):
            self.assertIn(phrase, flash)

    def test_flash_components_have_triggers_and_matching_evidence(self):
        components = self.read("references/flash-components.md")
        names = ("Behavioral Contract", "Evidence And Judgment Framework",
                 "Content And Structure Blueprint", "Action Contract")
        for name in names:
            section = components.split("## " + name + "\n", 1)[1].split("\n## ", 1)[0]
            with self.subTest(component=name):
                self.assertIn("**Use when:**", section)
                self.assertIn("**Completion evidence:**", section)
        for detail in ("Inputs and invocation", "Outputs", "State", "Examples", "Questions",
                       "Sources", "Criteria", "Uncertainty", "Audience", "Message", "Outline",
                       "Presentation", "Target", "Current-to-desired state", "Preconditions",
                       "Sequence", "Result confirmation"):
            self.assertIn(detail, components)

    def test_flash_software_routing_and_review_stay_optional(self):
        flash = self.read("references/flash-mode.md")
        routing = self.read("references/product-pattern-routing.md")
        discovery = self.read("references/cross-agent-compatibility.md")
        rubric = self.read("references/governance-review-rubrics.md")
        self.assertIn("they are not Flash's task components", flash)
        self.assertIn("do not need an app stack", flash)
        self.assertIn("do not reproduce a full file set", routing)
        self.assertIn("discovery does not require a Standard file set", discovery)
        self.assertIn("rubrics below apply to Standard and Retrofit", rubric)

    def test_flash_templates_are_optional_and_not_app_specific(self):
        plan = self.read("assets/flash-templates/PLAN.md")
        agents = self.read("assets/flash-templates/AGENTS.md")
        self.assertIn("Optional Flash starter", plan)
        self.assertIn("Optional Flash starter", agents)
        self.assertIn("## Outcome Contract", plan)
        self.assertIn("## Implementation Plan", plan)
        self.assertIn("## Evidence And Status", plan)
        self.assertNotIn("## Product Shape", plan + agents)
        self.assertNotIn("## Stack", plan + agents)
        self.assertIn("existing task/brief", plan)

    def test_flash_scenarios_are_explicit_static_walkthroughs(self):
        scenarios = self.read("references/flash-scenarios.md")
        names = ("usage_monitor: A Continuing Software Tool", "A Reusable Skill",
                 "Research Plus Slides", "A One-Off Document Edit", "Reschedule And Notify",
                 "A Weekly Analysis And Report Agent")
        for number, name in enumerate(names, 1):
            section = scenarios.split(f"## {number}. {name}\n", 1)[1].split("\n## ", 1)[0]
            with self.subTest(scenario=name):
                for label in ("Common contract", "Components", "Footprint", "Revisable plan", "Outcome checks"):
                    self.assertIn(f"**{label}:**", section)
        self.assertIn("do not report live actions", scenarios)
        self.assertIn("cannot demonstrate how a model selects components", scenarios)
        self.assertIn("Do not bootstrap `AGENTS.md`", scenarios)
        self.assertIn("These share one goal and context", scenarios)

    def test_three_language_entrypoints_link_flash_and_standard(self):
        for filename in ("README.md", "README_CN.md", "README_HK.md"):
            content = (self.root.parent / filename).read_text()
            with self.subTest(file=filename):
                for term in ("Standard", "Flash", "references/flash-mode.md", "references/flash-components.md",
                             "references/flash-scenarios.md", "assets/flash-templates/PLAN.md"):
                    self.assertIn(term, content)
        for filename in ("rookie-onboarding.md", "rookie-onboarding_CN.md", "rookie-onboarding_HK.md"):
            content = self.read("references/" + filename)
            with self.subTest(file=filename):
                for term in ("Standard", "Flash", "flash-mode.md"):
                    self.assertIn(term, content)

    def test_local_markdown_links_resolve(self):
        # Actual local Markdown destinations only; fenced sample project text is not a link manifest.
        for path in self.root.parent.rglob("*.md"):
            fenced = False
            for line in path.read_text().splitlines():
                if line.lstrip().startswith(("```", "~~~")):
                    fenced = not fenced
                    continue
                if fenced:
                    continue
                for destination in re.findall(r"\]\(([^)]+)\)", line):
                    target = destination.split(' "', 1)[0].strip("<>")
                    parsed = urlsplit(target)
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    with self.subTest(file=str(path.relative_to(self.root.parent)), link=target):
                        self.assertTrue((path.parent / unquote(parsed.path)).exists(), target)

    def test_sizing_and_retrofit_do_not_force_mechanical_stops(self):
        sizing = self.read("references/task-sizing.md")
        retrofit = self.read("references/retrofit-mode.md")
        self.assertIn("not an automatic stop or split", sizing)
        self.assertIn("no mandatory read-only session", retrofit)
        self.assertNotIn("Crossing three requires", sizing)
        self.assertNotIn("Spend one session purely reading", retrofit)

    def test_discovery_verification_does_not_rely_on_memory_editor(self):
        guide = self.read("references/cross-agent-compatibility.md")
        self.assertIn("`/memory` is not proof", guide)
        self.assertIn("Read a file in each required nested scope", guide)

    def test_opus_guidance_is_sourced_and_not_a_claim_of_evaluation(self):
        guide = self.read("references/frontier-model-guidance.md")
        self.assertIn("https://platform.claude.com/docs/en/", guide)
        self.assertIn("They cannot prove a model follows them", guide)
        self.assertIn("execution harness", guide)
        for path in ("assets/governance-templates/AGENTS.md", "assets/examples/feedback-inbox/AGENTS.md"):
            self.assertNotIn("Opus 5.5", self.read(path))


if __name__ == "__main__":
    unittest.main()
