import json
import tempfile
import unittest
from pathlib import Path

from argos_bridge.inventory import load_report_assets, summarize_assets


class InventoryTests(unittest.TestCase):
    def test_loads_report_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "report.json"
            path.write_text(
                json.dumps(
                    {
                        "report_id": "STU-001",
                        "name": "Active Registration",
                        "functional_area": "Student",
                        "sql_file": "sql_queries/student.sql",
                        "sensitivity": "FERPA",
                        "parameters": ["term_code"],
                        "business_question": "How many students are active?",
                    }
                ),
                encoding="utf-8",
            )

            assets = load_report_assets(tmp)

        self.assertEqual(1, len(assets))
        self.assertEqual("Student", assets[0].functional_area)
        self.assertEqual(["term_code"], assets[0].parameters)

    def test_summarizes_assets(self):
        assets = load_report_assets("reports")

        summary = summarize_assets(assets)

        self.assertGreaterEqual(summary["total_reports"], 4)
        self.assertIn("Student", summary["by_area"])
        self.assertGreaterEqual(summary["parameterized_reports"], 3)


if __name__ == "__main__":
    unittest.main()
