"""Regression tests for the public lint command; Python standard library only."""

from pathlib import Path
import subprocess
import tempfile
import unittest


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
    def run_lint(self, task=None, files=None):
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
                ["bash", str(SCRIPT), str(root)], text=True, capture_output=True
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

    def test_minimal_plan_is_explicitly_outside_lint_coverage(self):
        result = self.run_lint(files={"docs/PLAN.md": "# Plan\n"})
        self.assertIn("not structurally checked", result.stdout)
        self.assertNotIn("checks passed", result.stdout)

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

    def test_minimal_mode_exclusions_and_execution_contract(self):
        skill = self.read("SKILL.md")
        minimal = self.read("references/minimal-mode.md")
        self.assertIn("only when all safety exclusions", skill)
        self.assertIn("only when all of these safety exclusions", minimal)
        for phrase in ("No real or persistent user data", "No authentication, payments",
                       "No public API consumers", "No production deployment", "## Product Shape",
                       "### Interfaces", "Expected evidence:", "### Governance Drift"):
            self.assertIn(phrase, minimal)
        self.assertNotIn("at least three", skill + minimal)

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
