# Euro Exchange Pipeline

A simple Data Engineering project that extracts monthly USD/EUR exchange rate data from the European Central Bank API, transforms and validates the data using Python and Pandas, and stores the processed output as a CSV file.

## Project Goal

The goal of this project is to understand the basic structure of a Data Engineering pipeline and practice the ETL process:

- Extract data from an external API
- Transform raw XML data into a structured dataset
- Validate data quality
- Load the processed data into a CSV file

## Data Source

The project uses the European Central Bank Data API.

Current series:

- Currency: USD
- Reference currency: EUR
- Frequency: Monthly
- Dataset: Exchange Rates (EXR)

## Pipeline

```text
ECB API
   ↓
XML Response
   ↓
Python
   ↓
Data Extraction
   ↓
Pandas DataFrame
   ↓
Data Type Conversion
   ↓
Data Validation
   ↓
CSV Output