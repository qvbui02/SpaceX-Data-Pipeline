import singer
import pandas as pd
import requests

LOGGER = singer.get_logger()

schema = {
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'date_utc': {'type': 'string', 'format': 'date-time'}
    }
}

def main():
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    
    data = response.json()
    df = pd.DataFrame(data)  # Convert JSON data to DataFrame
    
    # Select relevant fields
    records = df[['id', 'name', 'date_utc']].to_dict(orient='records')

    singer.write_schema('launches', schema, 'id')
    singer.write_records('launches', records)

if __name__ == '__main__':
    main()
