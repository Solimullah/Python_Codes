# E-commerce QA Suite

This project is a comprehensive QA automation suite for an e-commerce website. It includes UI tests, API tests, and manual test cases.

## Tools and Technologies

*   **Python**: The primary programming language for writing the tests.
*   **PyTest**: The testing framework used to structure and run the tests.
*   **Selenium**: The browser automation framework used for UI testing.
*   **Requests**: The library used for making HTTP requests in the API tests.
*   **Allure**: The reporting tool used to generate detailed test reports.
*   **Postman/Newman**: The tools used for API testing and running collections from the command line.
*   **Docker**: The containerization platform used to run the tests in a consistent environment.
*   **GitHub Actions**: The CI/CD platform used to automate the test execution.

## Getting Started

### Prerequisites

*   Python 3.11
*   Docker
*   Node.js and npm (for Newman)

### Installation

1.  Clone the repository:
    ```
    git clone https://github.com/your-username/ecommerce-qa-suite.git
    ```
2.  Install the Python dependencies:
    ```
    pip install -r ecommerce-qa-suite/requirements.txt
    ```
3.  Install Newman:
    ```
    npm install -g newman
    ```

## Running Tests

### Locally

To run the tests locally, you can use the following commands:

*   **Run all tests:**
    ```
    pytest ecommerce-qa-suite/tests
    ```
*   **Run only UI tests:**
    ```
    pytest ecommerce-qa-suite/tests/ui
    ```
*   **Run only API tests:**
    ```
    pytest ecommerce-qa-suite/tests/api
    ```
*   **Run Postman tests:**
    ```
    ./ecommerce-qa-suite/scripts/run_postman_tests.sh
    ```

### With Docker

To run the tests in a Docker container, you can use the following command:
```
docker-compose up --build
```

## Test Strategy

The test strategy for this project is a combination of automated and manual testing.

*   **Automated Tests**:
    *   **UI Tests**: These tests cover the main user flows of the application, such as login, search, and checkout.
    *   **API Tests**: These tests cover the API endpoints for products, cart, and checkout.
*   **Manual Tests**: These tests cover the edge cases and scenarios that are difficult to automate.

## Viewing Reports

The test reports are generated using Allure. After running the tests, you can generate the report with the following command:
```
allure serve ecommerce-qa-suite/reports
```

The reports are also published to GitHub Pages after each run of the CI/CD pipeline. You can view the latest report at [https://your-username.github.io/ecommerce-qa-suite/](https://your-username.github.io/ecommerce-qa-suite/).
