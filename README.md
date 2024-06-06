# Repository Template

[![CI/CD Pull Request](https://github.com/nhs-england-tools/repository-template/actions/workflows/cicd-1-pull-request.yaml/badge.svg)](https://github.com/nhs-england-tools/repository-template/actions/workflows/cicd-1-pull-request.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=repository-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=repository-template)

Start with an overview or a brief description of what the project is about and what it does. For example -

Welcome to our repository template designed to streamline your project setup! This robust template provides a reliable starting point for your new projects, covering an essential tech stack and encouraging best practices in documenting.

This repository template aims to foster a user-friendly development environment by ensuring that every included file is concise and adequately self-documented. By adhering to this standard, we can promote increased clarity and maintainability throughout your project's lifecycle. Bundled within this template are resources that pave the way for seamless repository creation. Currently supported technologies are:

- Terraform
- Docker

Make use of this repository template to expedite your project setup and enhance your productivity right from the get-go. Enjoy the advantage of having a well-structured, self-documented project that reduces overhead and increases focus on what truly matters - coding!

## Table of Contents

- [Repository Template](#repository-template)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Configuration](#configuration)
  - [Usage](#usage)
    - [Testing](#testing)
  - [Design](#design)
    - [Diagrams](#diagrams)
    - [Modularity](#modularity)
  - [Contributing](#contributing)
  - [Contacts](#contacts)
  - [Licence](#licence)
  - [Setup Make in windows](#setup-make-in-windows)
- [WSL Set Up](#wsl-set-up)
  - [Windows WSL Installation](#windows-wsl-installation)
  - [Set up Visual Code to develop with WSL (optional)](#set-up-visual-code-to-develop-with-wsl-optional)
  - [Install pytest](#install-pytest)
  - [Git commits](#git-commits)
- [RAVS Playwright Pytest BDD Tests](#ravs-playwright-pytest-bdd-tests)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites-1)
    - [Installation](#installation)
  - [Docker](#docker)
    - [Build Docker Image](#build-docker-image)
    - [Run Docker Container](#run-docker-container)
    - [Usage](#usage-1)
    - [Configuration](#configuration-1)
    - [Folder Structure](#folder-structure)
    - [Test Run Report](#test-run-report)
  - [Contributing](#contributing-1)
  - [License](#license)

## Setup

By including preferably a one-liner or if necessary a set of clear CLI instructions we improve user experience. This should be a frictionless installation process that works on various operating systems (macOS, Linux, Windows WSL) and handles all the dependencies.

Clone the repository

```shell
git clone https://github.com/nhs-england-tools/repository-template.git
cd nhs-england-tools/repository-template
```

### Prerequisites

The following software packages, or their equivalents, are expected to be installed and configured:

- [Docker](https://www.docker.com/) container runtime or a compatible tool, e.g. [Podman](https://podman.io/),
- [asdf](https://asdf-vm.com/) version manager,
- [GNU make](https://www.gnu.org/software/make/) 3.82 or later,
- [GNU coreutils](https://www.gnu.org/software/coreutils/) and [GNU binutils](https://www.gnu.org/software/binutils/) may be required to build dependencies like Python, which may need to be compiled during installation. For macOS users, this has been scripted and automated by the `dotfiles` project; please see this [script](https://github.com/nhs-england-tools/dotfiles/blob/main/assets/20-install-base-packages.macos.sh) for details,
- [Python](https://www.python.org/) required to run Git hooks,
- [`jq`](https://jqlang.github.io/jq/) a lightweight and flexible command-line JSON processor.

> [!NOTE]<br>
> The version of GNU make available by default on macOS is earlier than 3.82. You will need to upgrade it or certain `make` tasks will fail. On macOS, you will need [Homebrew](https://brew.sh/) installed, then to install `make`, like so:
>
> ```shell
> brew install make
> ```
>
> You will then see instructions to fix your `$PATH` variable to make the newly installed version available. If you are using [dotfiles](https://github.com/nhs-england-tools/dotfiles), this is all done for you.

### Configuration

Installation and configuration of the toolchain dependencies

```shell
make config
```

## Usage

After a successful installation, provide an informative example of how this project can be used. Additional code snippets, screenshots and demos work well in this space. You may also link to the other documentation resources, e.g. the [User Guide](./docs/user-guide.md) to demonstrate more use cases and to show more features.

### Testing

There are `make` tasks for you to configure to run your tests.  Run `make test` to see how they work.  You should be able to use the same entry points for local development as in your CI pipeline.

## Design

### Diagrams

The [C4 model](https://c4model.com/) is a simple and intuitive way to create software architecture diagrams that are clear, consistent, scalable and most importantly collaborative. This should result in documenting all the system interfaces, external dependencies and integration points.

![Repository Template](./docs/diagrams/Repository_Template_GitHub_Generic.png)

### Modularity

Most of the projects are built with customisability and extendability in mind. At a minimum, this can be achieved by implementing service level configuration options and settings. The intention of this section is to show how this can be used. If the system processes data, you could mention here for example how the input is prepared for testing - anonymised, synthetic or live data.

## Contributing

Describe or link templates on how to raise an issue, feature request or make a contribution to the codebase. Reference the other documentation files, like

- Environment setup for contribution, i.e. `CONTRIBUTING.md`
- Coding standards, branching, linting, practices for development and testing
- Release process, versioning, changelog
- Backlog, board, roadmap, ways of working
- High-level requirements, guiding principles, decision records, etc.

## Contacts

Provide a way to contact the owners of this project. It can be a team, an individual or information on the means of getting in touch via active communication channels, e.g. opening a GitHub discussion, raising an issue, etc.

## Licence

> The [LICENCE.md](./LICENCE.md) file will need to be updated with the correct year and owner

Unless stated otherwise, the codebase is released under the MIT License. This covers both the codebase and any sample code in the documentation.

Any HTML or Markdown documentation is [© Crown Copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/) and available under the terms of the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## Setup Make in windows

Launch a new powershell window as an admin and run this command to install chocolatey

```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

Then install make using

```choco install make```

After installing make

```make githook-run```

# WSL Set Up

## Windows WSL Installation

[Install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

__Notes:__
- Unless otherwise specified, all commands are being run inside the Linux shell not Windows.
- Before we get started, Windows WSL users may wish to run this command (in the Linux shell) to set the default path to home. Alternatively set the path in windows terminal - this will allow multiple profiles:

```
echo -e '\n# Set default path to linux home directory\ncd ~' >> ~/.bashrc

source ~/.bashrc
```

- The WSL Ubuntu version might need openssl package to be updated, so run:

```
sudo apt upgrade && sudo apt update
```

(An out of date version of openssl will create problems with the self-signed certificate scripts.)

## Set up Visual Code to develop with WSL (optional)

[Configure Visual Studio Code to develop in WSL](VSCODE.md)

## Install pytest

```bash
pip install -U pytest
sudo apt-get update
sudo apt-get install jq
```
## Git commits

In order to make git commits to this repo, you need to use the following command in terminal

```bash
wsl
```
Need to configure git credentials in wsl and this is the command to make commits to the repo

```bash
PRE_COMMIT_ALLOW_NO_CONFIG=1 git commit -m "commit message"
```

# RAVS Playwright Pytest BDD Tests

This is a project for setting up and running end-to-end tests using Playwright, Pytest, and the Behavior-Driven Development (BDD) approach. It utilizes the dependency injection design pattern to provide a flexible and modular testing framework. It provides a flexible and modular testing framework, allowing for easy integration into future projects.

## Features

- **Playwright**: A Python library for automating browsers based on the powerful Playwright toolset.
- **Pytest**: A testing framework that makes it easy to write simple and scalable tests.
- **Behavior-Driven Development (BDD)**: A methodology for writing tests in simple, natural language constructs, making them more accessible to non-technical stakeholders.
- **Dependency Injection**: The project leverages the dependency injection design pattern to manage dependencies and promote code reusability and testability.

## Getting Started

### Prerequisites

- Python installed on your machine
- Pip package manager

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
## Docker

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
- pages
- Docker

### Test Run Report

The latest test run report can be found ([here](https://allure-report-ravs.netlify.app/#))

## Contributing

Contributions are welcome! If you have suggestions, improvements, or new features to add, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

