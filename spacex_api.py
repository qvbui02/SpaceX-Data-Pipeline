import pandas as pd
import requests

# fetch data from API
response = requests.get('https://api.spacexdata.com/v4/launches')

# convert response to json
data = response.json()

# convert json to DataFrame
df = pd.DataFrame(data)

print(df.head())