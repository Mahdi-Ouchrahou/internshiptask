import requests
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
from fastparquet import write
from alpha_vantage.techindicators import TechIndicators
import os


app = TechIndicators()
#help(app)
#L4CI4CSZE7LV83R3
API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
print(API_KEY)

#writing all paameters
param={
   "function" : "EMA",
   "symbol" : "IBM",
   "interval" : "daily",
   "time_period" : 100,
   "series_type" : "close",
   "datatype" : "csv",
   "apikey" : API_KEY,
 }
#saving the base url
url = 'https://www.alphavantage.co/query?'


#handling errors
try:
    #saving response in a variable r
    r = requests.get(url, params=param, timeout=5)
    r.raise_for_status()

    #code should be 200
    print(r.status_code)

    #saving the response in a string format in data and creating a csv file with that data
    data = r.text
    with open('output.csv', 'w+') as f:
        f.write(data)


    #here i converted csv file data into pandas data frame
    df = pd.read_csv('output.csv')
    print(df)

    #convert a pandas df to a compressed parquet file
    df.to_parquet('output.parquet', compression='snappy')
    pd.read_parquet('df.parquet.snappy')

except requests.exceptions.HTTPError as errh: #HTTP not found
    print(errh)
except requests.exceptions.ConnectionError as errc: #handle connection errors
    print(errc)
except requests.exceptions.Timeout as errt: #request takes many time to complete
    print(errt)
except requests.exceptions.RequestException as err:
    print(Err)
