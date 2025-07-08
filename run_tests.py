import pytest
import webbrowser
import os

report_path = os.path.join("reports", "report.html")

# run pytest and generate HTML report
pytest.main(["tests", f"--html={report_path}", "--self-contained-html"])

# open the report in the default web browser
webbrowser.open(f"file://{os.path.abspath(report_path)}")