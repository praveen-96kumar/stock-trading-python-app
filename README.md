# Polygon Stock Ticker Fetcher

A Python project to fetch and save active stock tickers from the Polygon.io API, handling pagination and saving results to a CSV file. The project includes scheduling support to run periodic updates.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Scheduling](#scheduling)
- [CSV Output](#csv-output)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project fetches active stock tickers data from the Polygon.io API, handles paginated responses automatically, and writes the ticker information such as ticker symbol, name, market, and other details to a CSV file named `tickers.csv`. It is designed for easy automation and updating of ticker lists.

## Features

- Fetches up to 1000 active stock tickers per API page with automatic pagination.
- Saves ticker data in CSV format with well-defined columns.
- Environment variable support for API key security.
- Optional task scheduling to run the data fetch at intervals using Python's schedule library.

## Tech Stack

- Python 3
- `requests` for API calls
- `python-dotenv` for environment variable management
- `schedule` for time-based task automation (optional)

## Setup Instructions

1. Clone the repository:

git clone <repo-url>
cd polygon-stock-ticker-fetcher

2. Create and activate a virtual environment (optional but recommended):

python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate

text

3. Install dependencies:
pip install -r requirements.txt

text

4. Obtain your Polygon API key from [Polygon.io](https://polygon.io/) and set it in a `.env` file at the root:
POLYGON_API_KEY=your_api_key_here

text

## Usage

Run the ticker fetching script:
python script.py

text
This will fetch active tickers and write them to `tickers.csv`.

## Scheduling

You can schedule periodic runs by using the `scheduler.py` script which leverages the `schedule` library.

Run:
python scheduler.py

text
Available schedules include every minute, every hour, and once daily at 9:00 AM by default. You can customize the timings within `scheduler.py`.

## CSV Output

The output CSV (`tickers.csv`) contains columns such as:
- `ticker`
- `name`
- `market`
- `locale`
- `primary_exchange`
- `type`
- `active`
- `currency_name`
- `cik`
- `composite_figi`
- `share_class_figi`
- `last_updated_utc`

This data can be used for further financial analysis or portfolio management.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/<your-username>/<repo-name>/issues) or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
