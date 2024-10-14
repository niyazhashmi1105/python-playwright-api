import re


def extract_test_results_from_text(file_path):
    # Define a regex pattern to match the test case name and status
    pattern = r"(.+?)\s+(PASSED|FAILED)"

    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    test_results = []

    # Open the text file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Use regex to find matches in each line
            match = re.search(pattern, line)
            if match:
                total_tests += 1
                test_case_name = match.group(1).strip()  # Extract the test case name
                test_status = match.group(2).strip()  # Extract the status (PASSED/FAILED)
                if test_status == 'PASSED':
                    test_results.append(f'<li style="color:green;">{test_case_name}: {test_status}</li>')
                    passed_tests += 1
                elif test_status == 'FAILED':
                    test_results.append(f'<li style="color:red;">{test_case_name}: {test_status}</li>')
                    failed_tests += 1
    return test_results,total_tests,passed_tests,failed_tests


# Example usage
if __name__ == '__main__':
    file_path = 'test_summary.txt'  # Replace with your actual file path

    # Extract the test results
    test_results,total_tests,passed_tests,failed_tests = extract_test_results_from_text(file_path)
    results = "\n".join(test_results)

    email_body = f"""
        <h2>API Automation Report:</h2>
        <p><strong>Total Test Cases:</strong> {total_tests}</p>
        <p><strong>Passed Test Cases:</strong> {passed_tests}</p>
        <p><strong>Failed Test Cases:</strong> {failed_tests}</p>
        <h3>Detailed Results:</h3>
        <ul>
            {''.join(test_results)}
        </ul>
        """

    # Save the email body to a file that will be used in GitHub Action
    with open('email_body.html', 'w') as file:
        file.write(email_body)
