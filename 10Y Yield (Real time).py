#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install quandl')


# In[3]:


import quandl
import matplotlib.pyplot as plt
import requests
import json
quandl.ApiConfig.api_key = 'y3g9qCEAwbkpskxytyU2'


# In[7]:


#column index: "1 MO","2 MO","3 MO","6 MO","1 YR","2 YR","3 YR","5 YR","7 YR","10 YR","20 YR","30 YR"
yc = quandl.get("USTREASURY/YIELD", start_date="2016-07-20", end_date="2023-01-20", column_index=10, collapse="monthly")

plt.plot(yc)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Yield', fontsize=14)
plt.title('US 10Y Yield')
plt.show()


# In[9]:


date = "2023-01-20"
r = quandl.get("USTREASURY/YIELD", start_date={date}, end_date={date}, column_index=10)
print(r)


symbol = 'PYPL'
key = '3MDNIU8UFGH66QG0'
#daily stock price
function = 'TIME_SERIES_DAILY_ADJUSTED'
url = requests.get(f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={key}").text
p = json.loads(url)
price = float(p['Time Series (Daily)']['2023-01-20']['5. adjusted close'])

f = price*(1+r)
print(f)


# In[ ]:




