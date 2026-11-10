"""Unit tests for the first learning example."""

import csv
import tempfile
import unittest
from pathlib import Path

from src.sensor_demo import generate_readings, save_readings


class SensorDemoTests(unittest.TestCase):
    def test_generates_expected_number_of_readings(self):
        self.assertEqual(len(generate_readings(10)), 10)

    def test_first_reading_is_as_expected(self):
        self.assertEqual(
            generate_readings(3)[0],
            {"time_s": 0, "temperature_c": 20.0},
        )

    def test_saves_csv_with_header_and_rows(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "measurements.csv"
            save_readings(generate_readings(2), path)
            with path.open(newline="", encoding="utf-8") as file:
                rows = list(csv.DictReader(file))
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[1]["time_s"], "1")


if __name__ == "__main__":
    unittest.main()
