Installation
To set up the framework, ensure you have Python installed on your system. Follow these steps to clone the repository and install dependencies:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
Folder Structure
Here's an overview of the folder structure in this project and the purpose of each directory and file:

bash
Copy code
.
├── .github/workflows/          # GitHub Actions workflows for CI/CD
├── .idea/                      # IDE settings (JetBrains IDEs)
├── __pycache__/                # Compiled Python files
├── data/                       # JSON or test data files
├── reports/                    # Directory for storing test reports
├── tests/                      # Test cases for the APIs
│   ├── test_booking_apis.py    # Test cases for booking APIs
│   └── test_user_apis.py       # Test cases for user-related APIs
├── utils/                      # Utility functions and helpers
│   ├── auth.py                 # Functions for handling authentication
│   ├── parse_report.py         # Functions to parse test reports
├── .gitignore                  # Git ignore file to exclude files/folders from version control
├── conftest.py                 # Configuration for pytest fixtures
├── globals.py                  # Global variables used across tests
├── parse_report.py             # Script to parse the test report
├── pytest.ini                  # Configuration file for pytest
└── requirements.txt            # List of required Python packages
Directory/File Descriptions
.github/workflows/: Contains the GitHub Actions workflows for CI/CD integration, which automate the testing process on push or pull request events.

.idea/: This folder contains configuration files for JetBrains IDEs (like PyCharm). It can be ignored in version control if you want to keep your workspace settings private.

pycache/: This folder stores compiled Python files to optimize loading times. It can be ignored in version control.

data/: Contains any JSON or test data files used in the tests.

reports/: This directory stores generated reports from test executions (e.g., HTML reports).

tests/: This folder includes all test scripts for different API endpoints.

test_booking_apis.py: Contains test cases specific to booking functionalities.
test_user_apis.py: Contains test cases for user-related functionalities.
utils/: This directory includes helper functions that can be used across multiple tests.

auth.py: Handles authentication-related functions.
parse_report.py: Contains functions to parse and extract information from the test reports.
.gitignore: Lists files and directories that should be ignored by Git. This typically includes environment files, IDE settings, and compiled Python files.

conftest.py: A special configuration file for pytest, where you can define fixtures, hooks, and configurations that can be used across your test files.

globals.py: A module to define global variables that can be accessed throughout the test scripts.

parse_report.py: This script is used to read and parse the test reports to extract relevant information, such as test case names and statuses.

pytest.ini: Configuration file for pytest, where you can set various options and parameters for your test runs.

requirements.txt: Contains a list of Python dependencies required to run the tests. Install them using pip install -r requirements.txt.

Usage
Create your test cases in the tests/ directory.

Use the utility functions from the utils/ directory as needed.

Run your tests using Pytest:

bash
Copy code
pytest tests/
Running Tests
You can run all tests with detailed output and generate an HTML report as follows:

bash
Copy code
pytest tests/ --html=reports/report.html --self-contained-html
Reporting
After running the tests, the HTML report can be found in the reports/ directory. You can parse the report using the provided utility functions in the utils/parse_report.py script.
