import requests
import json
import pandas as pd

# Calling API
response = requests.get("https://1ryu4whyek.execute-api.us-west-2.amazonaws.com/dev/skus")

# creating json data
data = response.json()

#creating json file for use later
with open("sku_data.json", "w") as file:
    json.dumps(data, file)

# creating dataframe from json file
df=pd.read_json('sku_data.json')

# filtering number of seconds between Jan 1, 1970 and Jan 1, 2022 which is 1,640,995,200
df2=df[df['createdAt']>=1640995200]

# find number of records after filtering
records = df2.shape[0]

# saving filtered data to json file
df2.to_json('sku_data_filtered.json')

# return number of records after filtering
print(f'The number of records on or after January 1, 2022 is {records}')