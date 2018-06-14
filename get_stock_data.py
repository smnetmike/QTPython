import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2016,1,1)
end = dt.datetime(2016,12,31)

#df = web.DataReader('TSLA', 'google', start, end)
df = pdr.get_data_yahoo('TSLA')
print(df.head())
