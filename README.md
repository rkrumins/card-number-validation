# Credit Card Validator

This repository contains a basic implementation of credit (debit) card validation.

## Pre-requisities

This repository contains the following dependencies:
- Python 3.9+

## Installation Steps

Please follow the steps below in order to setup the codebase
```bash
cd ${PROJECT_BASE_DIRECTORY}
# Ensure you are running the up-to-date PIP version
pip3 install --upgrade pip
# Create a virtual environment for the project
python3 -m venv env
# Activate virtual environment
source env/bin/activate
# Install dependencies
pip3 install -r requirements.txt
```

## Starting the webserver

```bash
cd ${PROJECT_BASE_DIRECTORY}
# Ensure you have the virtual environment activated
source env/bin/activate 
export FLASK_APP=server.py
# OPTIONAL: Enable debug mode
export FLASK_DEBUG=1
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
# Start the webserver
flask run --host=0.0.0.0 --port 4999
```

## Running unit tests

To run unit tests, please run below steps:

```bash
cd ${PROJECT_BASE_DIRECTORY}
cd tests
pytest
```

## Running unit tests with Code Coverage

To run unit tests, please run below steps:

```bash
cd ${PROJECT_BASE_DIRECTORY}/tests
coverage html
cd htmlcov
# After this proceed to open the index.html file
```

