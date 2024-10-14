from bs4 import BeautifulSoup


def extract_test_results(report_path):
    # Open and read the HTML report
    with open(report_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the test table that contains the results
    test_results = []

    # In pytest-html, test results are usually in a table with a specific class or structure
    for row in soup.find_all('tr', class_='passclass') + soup.find_all('tr', class_='failclass'):
        # Extract test case name and status
        test_case_name = row.find('td', class_='col-name').text.strip()
        test_status = 'Passed' if 'passclass' in row['class'] else 'Failed'

        test_results.append({
            'name': test_case_name,
            'status': test_status
        })

    return test_results


if __name__ == '__main__':
    # Path to the HTML report
    report_path = 'reports/report.html'

    # Extract the test results
    results = extract_test_results(report_path)

    # Format the results for embedding into the email
    results_summary = "\n".join([f"{result['name']}: {result['status']}" for result in results])

    # Print the summary to capture it in the GitHub Action
    print(results_summary)
