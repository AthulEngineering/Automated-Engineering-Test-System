# Automated Engineering Test System

## Project Overview
The Automated Engineering Test System is a Python-based application developed to automate the testing and analysis of engineering voltage measurements.

The application reads voltage data from a CSV file, checks each measurement against predefined limits, generates PASS/FAIL results, calculates statistical summaries, and produces a graphical analysis.

## Features
- Reads engineering test data from CSV files.
- Automatically checks voltage measurements against specified limits.
- Generates PASS/FAIL results for individual tests.
- Calculates average, minimum, and maximum voltage.
- Calculates the overall pass percentage.
- Saves test results into a CSV file.
- Generates voltage analysis graphs using Matplotlib.
- Handles missing files and invalid input data.
- Includes automated unit tests using pytest.

## Technologies Used
- Python
- CSV data processing
- Matplotlib
- Pytest

## Project Structure

Automated-Engineering-Test-System/
│
├── main.py
├── test_automation.py
├── test_data.csv
├── requirements.txt
├── README.md
├── results.csv
└── voltage_analysis.png

## Voltage Testing Limits

The system uses the following default voltage limits:

- Lower limit: 11.5 V
- Upper limit: 12.5 V

Measurements within this range are classified as PASS.
Measurements outside this range are classified as FAIL.

## Installation

1. Clone or download this repository.
2. Install the required Python packages:

   pip install -r requirements.txt

## Running the Application

Run the following command:

python main.py

The application processes the input data and generates test results and a voltage analysis graph.

## Running Automated Tests

Execute:

python -m pytest -v

The automated tests verify normal voltage measurements, high and low voltage conditions, and boundary values.

## Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and modular code development.
- Engineering data processing and analysis.
- Automated testing and validation.
- Error handling and input verification.
- Statistical calculations and graphical visualisation.

## Author
Athul R Bijith

## Disclaimer
This is an independent educational project developed to demonstrate the application of Python programming in engineering test automation. It is not a certified industrial testing system.