from datetime import datetime
import os


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list of strings.")

    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_str}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Success: Log written to {filename}")
    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
