# E-commerce Automation Testing Framework

A Selenium + Pytest automation testing framework for the Automation Exercise e-commerce website.

## Features

- **Page Object Model (POM)** design pattern for maintainable test code
- **Explicit Waits** using WebDriverWait for reliable element interactions
- **Pytest Parametrization** for data-driven testing
- **HTML Reports** with screenshots on test failures
- **GitHub Actions CI** for automated test execution
- **Comprehensive Test Coverage**:
  - Authentication and login validation
  - Product catalog and search functionality
  - Cart operations (add, remove, persistence)
  - Checkout flow and payment validation
  - Negative test cases and boundary conditions

## Prerequisites

- Python 3.12+
- Chrome Browser
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/murugavelvv/auto_exercise.git
cd auto_exercise
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
auto_exercise/
├── base.py                 # BasePage class with common methods
├── conftest.py             # Pytest fixtures and hooks
├── login_page.py           # Login page object
├── product_page.py         # Product page object
├── checkout_page.py        # Checkout page object
├── test_login.py           # Login test cases
├── test_product.py         # Product test cases
├── test_cart.py            # Cart test cases
├── test_checkout_negative.py # Negative checkout test cases
├── test_e2e_checkout.py    # End-to-end checkout test
├── .github/
│   └── workflows/
│       └── pytest.yml      # GitHub Actions CI workflow
└── requirements.txt         # Python dependencies
```

## Running Tests

### Run all tests locally:
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run tests in parallel (faster execution):
```bash
pip install pytest-xdist
pytest -n 3 --html=reports/report.html --self-contained-html
```

### Run specific test file:
```bash
pytest test_login.py --html=reports/report.html
```

### Run specific test:
```bash
pytest test_login.py::test_valid_login --html=reports/report.html
```

## Test Reports

After test execution, an HTML report is generated at `reports/report.html` with:
- Test execution summary
- Pass/fail status for each test
- Screenshots of failures (if any)
- Execution time

## CI/CD

Tests automatically run on GitHub Actions when code is pushed to the `main` branch. View the results in the **Actions** tab of the repository.

## Technologies Used

- **Selenium WebDriver** - Browser automation
- **Pytest** - Test framework
- **pytest-html** - HTML reporting
- **webdriver-manager** - Chrome driver management
- **Page Object Model** - Design pattern

## Test Credentials

- Email: `vmurugavel877@gmail.com`
- Password: `muru@123`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure they pass
5. Submit a pull request

## License

This project is open source and available under the MIT License.
