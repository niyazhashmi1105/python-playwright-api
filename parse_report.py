import re


def extract_test_results_from_text(file_path):
    # Define a regex pattern to match the test case name and status
    pattern = r"(.+?)\s+(PASSED|FAILED)"

    test_results = []

    # Open the text file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Use regex to find matches in each line
            match = re.search(pattern, line)
            if match:
                test_case_name = match.group(1).strip()  # Extract the test case name
                test_status = match.group(2).strip()  # Extract the status (PASSED/FAILED)
                test_results.append(f"<li>{test_case_name}: {test_status}</li>")

    return test_results


# Example usage
if __name__ == '__main__':
    file_path = 'test_summary.txt'  # Replace with your actual file path

    # Extract the test results
    results = extract_test_results_from_text(file_path)

    if results:
        print("\n".join(results))  # Joining results with newline for clarity
    else:
        print("No test results found.")
