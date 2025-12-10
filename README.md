# VocaVolt Automation Testing

Automated test suite for the VocaVolt language learning platform using Selenium WebDriver and Python.

## Project Overview

This repository contains automated UI tests for the VocaVolt website, specifically focusing on the login functionality and user authentication flows. The tests are designed to ensure the reliability and security of the login process.

## Test Coverage

### Functional Tests
- Valid login with correct credentials
- Invalid email format handling
- Incorrect password validation
- Empty field validation
- Partial field validation (email only, password only)

### Security Tests
- SQL injection attempts
- Cross-site scripting (XSS) attacks
- Special character handling in credentials
- Case sensitivity testing
- Long credential input validation
- Whitespace-only field validation

### Black Box Testing
- UI element presence verification
- Password field masking validation
- Form validation behavior
- Redirect functionality testing

### Gray Box Testing
- Session handling after successful login
- Error message consistency analysis
- Input field validation timing
- Browser navigation behavior

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- Internet connection (for initial driver setup)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd vocavolt-automation-testing
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The tests can be configured using environment variables:

- `CHROMEDRIVER_PATH`: Path to local ChromeDriver executable
- `GECKODRIVER_PATH`: Path to local GeckoDriver executable (for Firefox)
- `BROWSER`: Browser to use for testing (default: chrome, options: chrome, firefox)

## Running Tests

### Run all login tests:
```bash
python -m pytest tests/test_login.py
```

### Run tests with verbose output:
```bash
python -m pytest tests/test_login.py -v
```

### Run tests with detailed output:
```bash
python -m pytest tests/test_login.py -vv
```

### Run tests and show print statements:
```bash
python -m pytest tests/test_login.py -s
```

### Run specific test:
```bash
python -m pytest tests/test_login.py::test_valid_login
```
### Run specific test:
```bash
pytest --cov=. --cov-report=html
```

## Test Structure

```
tests/
├── test_login.py          # Main login test suite
pages/
├── login_page.py          # Page Object Model for login page
├── sections_page.py       # Page Object Model for sections page
utils/
├── driver_factory.py      # WebDriver management
```

## Page Object Models

### LoginPage
- Locator definitions for email, password, and login button
- Methods for entering credentials and submitting login form

### SectionsPage
- Locator definitions for section elements
- Methods for navigating to lessons

## Continuous Integration

The test suite is designed to be CI/CD friendly and can be integrated with popular CI platforms like Jenkins, GitHub Actions, or GitLab CI.

## Troubleshooting

### WebDriver Issues
If you encounter connection errors when running tests:
1. Ensure you have an internet connection for initial driver download
2. Download ChromeDriver manually and set `CHROMEDRIVER_PATH` environment variable
3. Alternatively, use Firefox by setting `BROWSER=firefox`

### Test Failures
Common reasons for test failures:
- Incorrect credentials in test data
- Changes to website UI elements
- Network connectivity issues
- Browser compatibility issues

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your tests or modifications
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Selenium WebDriver for browser automation
- pytest for test framework
- WebDriver Manager for automatic driver management