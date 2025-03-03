import pandas as pd

data = {
    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy',
    ],
    'launches': [5, 100, 3]
}

# create DataFrame using pandas
df = pd.DataFrame(data)

# accessing a column
df['rocket']

# fitlering row
falcon9_df = df[df['rocket'] == 'Falcon 9']

# adding new column
df['success_rate'] = [0.4, 0.98, 1.0]

print(df)