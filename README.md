# QA Automation Framework

A comprehensive test automation framework built with Python, Selenium, and Behave for BDD testing.

## Features

- **BDD Testing** with Behave framework
- **Cross-browser testing** with Selenium WebDriver
- **Data-driven testing** with Excel/CSV support
- **Allure reporting** for detailed test reports
- **API testing** capabilities
- **Code quality** tools (Black, Flake8)
- **Pre-commit hooks** for code consistency
- **Multiple environment management** with Tox

## Prerequisites

- Python 3.11 or higher
- Chrome browser (for default configuration)
- Git

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ptilak27/qa-automation.git
cd qa-automation
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Install pre-commit hooks (optional but recommended)
```bash
pre-commit install
```

## Project Structure

```
qa-automation/
├── automation/
│   └── tests/
│       └── features/         # BDD feature files
│           └── api/
│           └── steps/
│           └── ui/
├── pages/                    # Page Object Model files
├── utils/                    # Utility functions
├── data/
│   └── users.xlsx            # Test data files
├── reports/                  # Test reports
│   ├── allure-results/       # Allure results
│   └── allure-report/        # Generated Allure reports
├── config.yaml               # Configuration file
├── requirements.txt          # Python dependencies
└── tox.ini                  # Tox configuration
```

## Configuration

The project uses `config.yaml` for configuration settings:

- **Base URLs**: Amazon India and API endpoints
- **Browser settings**: Chrome (non-headless by default)
- **Test data**: Excel file paths
- **Logging**: INFO level with timestamp format
- **Reports**: Output directories for results

## Running Tests

### Using Tox (Recommended)

Tox provides isolated environments and multiple testing scenarios:

#### Run all tests
```bash
tox
```

#### Run specific environments
```bash
# Run BDD tests with pretty formatting
tox -e behave

# Run tests with Allure reporting
tox -e behave-allure

# Run linting
tox -e lint

# Check code formatting
tox -e format

# Auto-format code
tox -e format-fix

# Run pre-commit hooks
tox -e pre-commit
```

### Direct Behave Commands

#### Basic test execution
```bash
behave automation/tests/features
```

#### Run with specific tags
```bash
# Skip work-in-progress tests
behave automation/tests/features --tags=-wip

# Run only smoke tests (if tagged)
behave automation/tests/features --tags=smoke
```

#### Run with different formatters
```bash
# Pretty format
behave -f pretty automation/tests/features

# JUnit format
behave --junit automation/tests/features

# HTML report
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html automation/tests/features
```

## Reporting

### Allure Reports

1. **Generate Allure results:**
```bash
behave automation/tests/features -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

2. **Generate and serve Allure report:**
```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure serve reports/allure-results
```

### HTML Reports

Generate HTML reports using behave-html-formatter:
```bash
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html automation/tests/features
```

## Code Quality

### Linting
```bash
# Run flake8 linting
flake8 automation/tests/features pages utils --max-line-length=100

# Or use tox
tox -e lint
```

### Code Formatting
```bash
# Check formatting
black --check --diff automation/tests/features pages utils

# Auto-format
black automation/tests/features pages utils

# Or use tox
tox -e format        # Check only
tox -e format-fix    # Auto-format
```

## Development Workflow

1. **Write your feature files** in `automation/tests/features/`
2. **Implement step definitions** and page objects
3. **Add test data** to `data/users.xlsx` or create new data files
4. **Run tests locally:**
   ```bash
   tox -e behave
   ```
5. **Check code quality:**
   ```bash
   tox -e lint
   tox -e format
   ```
6. **Generate reports:**
   ```bash
   tox -e behave-allure
   ```

## Environment Variables

You can override configuration using environment variables:

```bash
export BROWSER_NAME=firefox
export HEADLESS=true
export BASE_URL=https://custom-url.com
```
