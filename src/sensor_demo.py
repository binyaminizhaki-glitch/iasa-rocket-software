"""Generate and save simulated sensor readings for a first team exercise."""

import csv
from pathlib import Path


def generate_readings(count=10):
    """Return deterministic simulated temperature readings."""
    return [
        {"time_s": second, "temperature_c": round(20 + 0.5 * second, 1)}
        for second in range(count)
    ]


def save_readings(readings, path):
    """Save readings to a CSV file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["time_s", "temperature_c"])
        writer.writeheader()
        writer.writerows(readings)


if __name__ == "__main__":
    destination = Path("output") / "simulated_sensor_data.csv"
    save_readings(generate_readings(), destination)
    print(f"Saved simulated readings to {destination}")
