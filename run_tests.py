import pytest
import os
from test_list import test_files   # import the list

def run_selected_tests():
    os.makedirs("reports", exist_ok=True)

    for test_file in test_files:
        base_name = os.path.basename(test_file).replace(".py", "")
        report_file = f"reports/{base_name}_report.html"

        print(f"Running {test_file} → {report_file}")

        pytest.main([
            test_file,
            "-vs",
            f"--html={report_file}",
            "--self-contained-html"
        ])

if __name__ == "__main__":
    run_selected_tests()
