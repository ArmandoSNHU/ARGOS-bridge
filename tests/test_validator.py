import tempfile
import unittest
from pathlib import Path

from argos_bridge.validator import validate_sql_file, validate_sql_standards


class ValidatorTests(unittest.TestCase):
    def test_valid_sql_passes_without_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "valid.sql"
            path.write_text("SELECT id FROM SC_ERP.STUDENTS;", encoding="utf-8")

            issues = validate_sql_file(path)

        self.assertFalse([issue for issue in issues if issue.severity == "ERROR"])

    def test_dangerous_sql_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "dangerous.sql"
            path.write_text("DROP TABLE SC_ERP.STUDENTS;", encoding="utf-8")

            issues = validate_sql_file(path)

        self.assertTrue(any(issue.severity == "ERROR" for issue in issues))

    def test_missing_semicolon_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "missing_semicolon.sql"
            path.write_text("SELECT id FROM SC_ERP.STUDENTS", encoding="utf-8")

            issues = validate_sql_file(path)

        self.assertTrue(any("semicolon" in issue.message for issue in issues))

    def test_select_star_is_warning_not_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "select_star.sql"
            path.write_text("SELECT * FROM SC_ERP.STUDENTS;", encoding="utf-8")

            issues = validate_sql_file(path)

        self.assertTrue(any(issue.severity == "WARNING" for issue in issues))
        self.assertFalse(any(issue.severity == "ERROR" for issue in issues))

    def test_directory_report_tracks_checked_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "one.sql").write_text("SELECT id FROM SC_ERP.STUDENTS;", encoding="utf-8")
            Path(tmp, "two.sql").write_text("SELECT id FROM SC_ERP.COURSES;", encoding="utf-8")

            report = validate_sql_standards(tmp)

        self.assertEqual(2, report.checked_files)
        self.assertTrue(report.passed)


if __name__ == "__main__":
    unittest.main()
