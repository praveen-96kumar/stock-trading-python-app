import requests
import os
import csv
import time
from dotenv import load_dotenv

load_dotenv()



POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

LIMIT = 10
#this is the url for the polygon api to get the tickers
url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
#response = requests.get(url) # this is the response from the polygon api , if not loop required and the default can be upto 1000
#print(response.json())
response = requests.get(url)
tickers = []


data = response.json()

# Check if API returned an error
if data.get('status') == 'ERROR':
    print(f"API Error: {data.get('error', 'Unknown error')}")
    exit(1)

# Check if 'results' key exists
if 'results' not in data:
    print("Error: 'results' key not found in API response")
    print("Response:", data)
    exit(1)

#print(data.keys()) for checking the keys of the response, as 1st instance is a key and 2nd instance is a list of tickers
for ticker in data['results']:
    tickers.append(ticker)

while 'next_url' in data:
    print('requesting next page',data['next_url'])
    
    # Add delay to avoid rate limiting
    time.sleep(1)  # Wait 1 second between requests
    
    response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
    data = response.json()
    
    # Check if API returned an error
    if data.get('status') == 'ERROR':
        print(f"API Error: {data.get('error', 'Unknown error')}")
        print("Stopping pagination due to error")
        break
    
    # Check if 'results' key exists
    if 'results' not in data:
        print("Error: 'results' key not found in subsequent page")
        print("Response:", data)
        break
    
    print(f"Found {len(data['results'])} tickers in this page")
    for ticker in data['results']:
        tickers.append(ticker)

example_ticker = {'ticker': 'HTHT', 
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
 'last_updated_utc': '2025-09-18T06:05:34.657274843Z'}

# Write tickers to CSV with example ticker
fieldnames = list(example_ticker.keys())    
output_csv = 'tickers.csv'
with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for t in tickers:
        row = {key: t.get(key, '') for key in fieldnames}
        writer.writerow(row)
print(f'wrote {len(tickers)} row to {output_csv}')        



