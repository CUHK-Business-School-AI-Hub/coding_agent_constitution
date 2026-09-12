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

    def test_bundled_example_remains_compatible(self):
        result = subprocess.run(["bash", str(SCRIPT), str(EXAMPLE)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("ERROR", result.stdout)


if __name__ == "__main__":
    unittest.main()
