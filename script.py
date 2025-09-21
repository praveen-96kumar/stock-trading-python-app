import requests
import os
import csv
import time
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
LIMIT = 1000

example_ticker = {
    'ticker': 'HTHT',
    'name': 'H World Group Limited American Depositary Shares',
    'market': 'stocks',
    'locale': 'us',
    'primary_exchange': 'XNAS',
    'type': 'ADRC',
    'active': True,
    'currency_name': 'usd',
    'cik': '0001483994',
    'composite_figi': 'BBG000QFPM65',
    'share_class_figi': 'BBG001T6Y5T2',
    'last_updated_utc': '2025-09-18T06:05:34.657274843Z'
}

def run_stock_job():
    url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
    tickers = []

    while url:
        response = requests.get(url)
        data = response.json()

        # Append tickers from current page
        for ticker in data.get('results', []):
            tickers.append(ticker)

        # Check for next page URL for pagination
        url = data.get('next_url')
        if url:
            url = url + f'&apiKey={POLYGON_API_KEY}'
            print(f"Requesting next page: {url}")
            time.sleep(12)  # Respect 5 requests/min rate limit

    # Write tickers to CSV
    fieldnames = list(example_ticker.keys())
    output_csv = 'tickers.csv'
    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for t in tickers:
            row = {key: t.get(key, '') for key in fieldnames}
            writer.writerow(row)

    print(f"Wrote {len(tickers)} rows to {output_csv}")

if __name__ == '__main__':
    run_stock_job()