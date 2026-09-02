import pytest
import os
from datetime import datetime
from test_list import test_files


def run_selected_tests():
    os.makedirs("reports", exist_ok=True)

    for test_file in test_files:

        # Get test file name
        file_name = os.path.splitext(os.path.basename(test_file))[0]

        # Generate date + time
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]

        # Create unique report name
        report_file = os.path.join(
            "reports",
            f"{file_name}_{timestamp}.html"
        )

        print(f"\nRunning: {test_file}")
        print(f"Report:  {report_file}\n")

        pytest.main([
            test_file,
            "-vs",
            f"--html={report_file}",
            "--self-contained-html"
        ])


if __name__ == "__main__":
    run_selected_tests()