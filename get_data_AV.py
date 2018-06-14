import requests
import pandas as pd
import io

url = "https://www.alphavantage.co/query"

function = "TIME_SERIES_DAILY_ADJUSTED"
symbol = "RGLD"
api_key = "41LNM3QTUMSUIDX8"
data_type = "csv"
output_size = "compact" 

data = { "function": function,
         "symbol": symbol,
         "apikey": api_key,
         "datatype": data_type,
         "outputsize": output_size}
page = requests.get(url, params = data)
df = pd.read_csv(io.StringIO(page.text))
print(df.head())
