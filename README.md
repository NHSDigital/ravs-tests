# RAVS Playwright Pytest BDD Tests

This is a project for setting up and running end-to-end tests using Playwright, Pytest, and the Behavior-Driven Development (BDD) approach. It utilizes the dependency injection design pattern to provide a flexible and modular testing framework, allowing for easy integration into future projects.

## Features

- **Playwright**: A Python library for automating browsers based on the powerful Playwright toolset.
- **Pytest**: A testing framework that makes it easy to write simple and scalable tests.
- **Behavior-Driven Development (BDD)**: A methodology for writing tests in simple, natural language constructs, making them more accessible to non-technical stakeholders.
- **Dependency Injection**: The project leverages the dependency injection design pattern to manage dependencies and promote code reusability and testability.

## Getting Started

### Prerequisites

- Python installed on your machine
- Pip package manager
- VS code installed
- VS code plugins needed
  - Test explorer UI
  - Python
  - Playwright test for VSCode
  - Test adapter converter

> **Note:** If tests do not load in Test Explorer, restart VS Code and that should fix the issue.

## Install pytest

```bash
pip install -U pytest
sudo apt-get update
sudo apt-get install jq
```

## Git commits

  In order to make git commits to this repo, you need to use the following command in terminal

  ```bash
  PRE_COMMIT_ALLOW_NO_CONFIG=1 git commit -m "commit message"
  ```

### Installation

1. Clone this repository:

```bash
  git clone git@github.com:NHSDigital/ravs-tests.git
```

2. Navigate to the project directory:

```bash
  cd ravs-tests
```

3. Install dependencies:

```bash
  pip install -r requirements.txt
```

## Running tests

### Mac OS

```bash
export RAVS_PASSWORD="$RAVS_PASSWORD"
export HEADLESS_MODE="false"
export TEST_ENVIRONMENT="dev"
export BROWSER="edge"
export DEVICE="iphone_12"
export MARKER="login"
export AGENTS=3

tox -v # or pytest
```

### Windows

```bash
$env:RAVS_PASSWORD = $env:RAVS_PASSWORD
$env:HEADLESS_MODE = "false"
$env:TEST_ENVIRONMENT= "dev"
$env:BROWSER= "edge"
$env:DEVICE= "iphone_12"
$env:MARKER= "login"
$env:AGENTS= 3

tox -v # or pytest
```

## Docker (Optional setup)

### Build Docker Image

Build the Docker image using the following command:

```bash
docker build -t your_docker_image_name -f Docker/tests.dockerfile .
```

### Run Docker Container

Run the Docker container using the following command:

```bash
docker run -it -p 5050:5050 \
  -e RAVS_PASSWORD=$env:RAVS_PASSWORD \
  -e HEADLESS_MODE="true" \
  -e TEST_ENVIRONMENT="qa" \
  -e BROWSER="chrome" \
  -e DEVICE="iphone_12" \
  -e MARKER="login" \
  -e AGENTS=3 \
  your_docker_image_name
```

Replace your_docker_image_name with the desired name for your Docker image. This command will run the Docker container with the specified environment variables, including the password, headless mode, test environment, browser, and device configuration.

### Usage

1. Write your feature files using Gherkin syntax in the `features` directory.
2. Implement your step definitions in the `steps` directory using Python.
3. Run the tests using the following command:

    ```bash
    # For Windows
    scoop install allure

    # For Linux
    apt-get update && apt-get install -y allure

    # Set the password, headless mode, test environment, and browser variables and run the tests
    $env:RAVS_PASSWORD = "YourPasswordHere"; $env:HEADLESS_MODE = "false"; $env:TEST_ENVIRONMENT= "qa"; $env:BROWSER= "chrome"; $env:DEVICE= "iphone_12" ; $env:MARKER= "" ; $env:AGENTS= 3 tox
    ```

### Configuration

- Modify the `pytest.ini` file to configure Pytest options and plugins.
- Update the `tox.ini` file to define the test environments and configurations.

### Folder Structure

- features
- steps
- pages
- helpers
- Docker

### Test Run Report

The latest test run report can be found ([here](https://nhsdigital.github.io/ravs-test-reports/RAVS/dev/edge/#))

## Contributors

- [@neelimaguntpalli1-nhs](https://github.com/neelimaguntpalli1-nhs) – Initial framework setup (no longer active on project)

## Contributing

Contributions are welcome! If you have suggestions, improvements, or new features to add, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
