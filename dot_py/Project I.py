#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys 
import fire
import csv
import questionary
import pandas as pd 
from pathlib import Path

import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go


# In[5]:


#Read in the CSV file called "TRX_USD.csv" using the path module. 
trx_path = Path('../csv_data/csv_files_crypto/TRX_USD.csv')

#Read trx csv into pandas dataframe, indexing date.
trx_df = pd.read_csv(
        trx_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)
trx_df.head()


# In[14]:


#Verify 'close' data-type as "float."
trx_df.dtypes


# In[15]:


#Filter out 'close' price into a sliced dataframe. 
trx_sliced = trx_df.iloc[:,[3]]


# In[16]:


#Rename 'close' price to 'TRX/USD' in a new dataframe.
trx_new = trx_sliced.rename(columns={"Close":'TRX/USD'})

#Review the top 5 results of dataframe. 
trx_new.head()


# In[17]:


#Read in the CSV file called "BTC_USD.csv" using the path module.
btc_path = Path('../csv_data/csv_files_crypto/BTC_USD.csv')

#Read btc csv into pandas dataframe, indexing date.
btc_df = pd.read_csv(
        btc_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)


# In[18]:


#Verify 'close' data-type as "float." 
btc_df.dtypes


# In[19]:


#Filter out 'close' price into sliced dataframe. 
btc_sliced = btc_df.iloc[:,[3]]


# In[20]:


#Rename 'close' price to 'BTC/USD' in a new dataframe.
btc_new = btc_sliced.rename(columns={"Close":"BTC/USD"})

#Display the top 5 results.
btc_new.head()


# In[21]:


#Read in the CSV file called "ETH_USD.csv" using the path module. 
eth_path = Path('../csv_data/csv_files_crypto/ETH_USD.csv')

#Read eth csv into pandas dataframe, indexing date.
eth_df = pd.read_csv(
        eth_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)


# In[22]:


#Verify 'close' data-type as "float." 
eth_df.dtypes


# In[23]:


#Filter out 'close' price into sliced dataframe. 
eth_sliced=eth_df.iloc[:,[3]]


# In[24]:


#Rename 'close' price to 'ETH/USD' in a new dataframe.
eth_new = eth_sliced.rename(columns={"Close":"ETH/USD"})

#Review top 5 results.
eth_new.head()


# In[25]:


#Read in the CSV file called "XLM_USD.csv" using the path module. 
xlm_path = Path('../csv_data/csv_files_crypto/XLM_USD.csv')

#Read xlm csv into pandas dataframe, indexing date.
xlm_df = pd.read_csv(
        xlm_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)


# In[26]:


#Verify 'close' data-type as float. 
xlm_df.dtypes


# In[27]:


#Filter out 'close' price into sliced dataframe. 
xlm_sliced = xlm_df.iloc[:,[3]]


# In[28]:


#Rename 'close' price to 'XLM/USD' in a new dataframe. 
xlm_new = xlm_sliced.rename(columns={"Close":"XLM/USD"})

#Review the top 5 results.
xlm_new.head()


# In[29]:


#Read in the CSV file called "XMR_USD.csv" using the path module. 
xmr_path = Path('../csv_data/csv_files_crypto/XMR_USD.csv')

#Read xmr csv into pandas dataframe, indexing date.
xmr_df = pd.read_csv(
        xmr_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)


# In[30]:


#Verify 'close' data-type as "float."
xmr_df.dtypes


# In[31]:


#Filter out 'close' price into sliced dataframe. 
xmr_sliced = xmr_df.iloc[:,[3]]


# In[32]:


#Rename 'close' price to 'XMR/USD' in a new dataframe.
xmr_new = xmr_sliced.rename(columns={"Close":"XMR/USD"})

#Display the top 5 results.
xmr_new.head()


# In[33]:


#Use concatenate function to group btc_new, eth_new, trx_new, xlm_new, xmr_new dataframes into a single dataframe called 'crypto.'
crypto = pd.concat([btc_new, eth_new, trx_new, xlm_new, xmr_new], axis=1)
#Display results. 
crypto


# In[34]:


crypto_daily_returns = crypto.pct_change()
crypto_daily_returns.head()


# In[ ]:


#Define the stimulus amount in a new variable.
starting_value = float(input("Starting amount"))


# In[ ]:


starting_value


# In[ ]:


#Calculate daily returns for xlm in a new dataframe. 
xlm_daily_returns = xlm_new.pct_change()

xlm_daily_returns.head()


# In[ ]:


#Add an empty portfolio column to XLM Daily Returns. 
xlm_daily_returns['Portfolio'] = pd.NaT

xlm_daily_returns


# In[ ]:


#Calculate the portfolio value over time. 
xlm_daily_returns = xlm_daily_returns.assign(Portfolio=(1+xlm_daily_returns['XLM/USD'].fillna(0)).cumprod().mul(starting_value))


# In[ ]:


#Rename columns. 
xlm = xlm_daily_returns.rename(columns={'XLM/USD':'XLM Daily Returns',"Portfolio":"XLM Port"})


# In[ ]:


#Display results. 
xlm.head()


# In[ ]:





# In[ ]:


#Calculate daily returns for XMR in a new dataframe. 
xmr_daily_returns = xmr_new.pct_change()


# In[ ]:


#Add an empty portfolio column to XMR Daily Returns. 
xmr_daily_returns['Portfolio'] = pd.NaT

xmr_daily_returns


# In[ ]:


#Calculate the portfolio value over time. 
xmr_daily_returns = xmr_daily_returns.assign(Portfolio=(1+xmr_daily_returns['XMR/USD'].fillna(0)).cumprod().mul(starting_value))


# In[ ]:


#Rename columns. 
xmr = xmr_daily_returns.rename(columns={'XMR/USD':'XMR Daily Returns',"Portfolio":"XMR Port"})


# In[ ]:


#Display results.
xmr.head()


# In[ ]:





# In[ ]:


#Calculate daily returns for ETH in a new dataframe. 
eth_daily_returns = eth_new.pct_change()


# In[37]:


#Add an empty portfolio column to ETH Daily Returns. 
eth_daily_returns['Portfolio'] = pd.NaT

eth_daily_returns


# In[38]:


#Calculate the portfolio value over time. 
eth_daily_returns = eth_daily_returns.assign(Portfolio=(1+eth_daily_returns['ETH/USD'].fillna(0)).cumprod().mul(starting_value))


# In[39]:


#Rename columns. 
eth = eth_daily_returns.rename(columns={'ETH/USD':'ETH Daily Returns',"Portfolio":"ETH Port"})


# In[40]:


#Display results.
eth.tail()


# In[ ]:





# In[41]:


#Calculate daily returns for BTC in a new dataframe. 
btc_daily_returns = btc_new.pct_change()


# In[42]:


#Add an empty portfolio column to BTC Daily Returns. 
btc_daily_returns['Portfolio'] = pd.NaT

btc_daily_returns


# In[43]:


#Calculate the portfolio value over time. 
btc_daily_returns = btc_daily_returns.assign(Portfolio=(1+btc_daily_returns['BTC/USD'].fillna(0)).cumprod().mul(starting_value))


# In[44]:


#Rename columns. 
btc = btc_daily_returns.rename(columns={'BTC/USD':'BTC Daily Returns',"Portfolio":"BTC Port"})


# In[45]:


#Display results.
btc.tail()


# In[ ]:





# In[46]:


#Calculate daily returns for TRX in a new dataframe. 
trx_daily_returns = trx_new.pct_change()


# In[47]:


#Add an empty portfolio column to TRX Daily Returns. 
trx_daily_returns['Portfolio'] = pd.NaT

trx_daily_returns


# In[48]:


#Calculate the portfolio value over time. 
trx_daily_returns = trx_daily_returns.assign(Portfolio=(1+trx_daily_returns['TRX/USD'].fillna(0)).cumprod().mul(starting_value))


# In[49]:


#Rename columns. 
trx = trx_daily_returns.rename(columns={'TRX/USD':'TRX Daily Returns',"Portfolio":"TRX Port"})


# In[50]:


#Display results.
trx.tail()


# In[ ]:





# In[51]:


#Use concatenate function to group the daily_returns and port values into one dataframe. 
crypto_new = pd.concat([btc, eth, trx, xmr, xlm],axis=1)

#Display results.
crypto_new


# In[52]:


crypto_new.plot()


# In[53]:


#Drop 'Daily Returns' column. 
crypto_sliced = crypto_new.iloc[:,[1,3,5,7,9]]
crypto_sliced


# In[6]:


#Build a figure for all series
fig = px.line(crypto_sliced, x=crypto_sliced.index, y = crypto_sliced.columns)
#Map lines/series to groups
maps = {'group 1': ['BTC Port', 'ETH Port'],
           'group 2':['TRX Port', 'XMR Port', "XLM Port"]}

#Create group and trace visibilites
group = []
vis = []
visList = []
for m in maps.keys():
    for col in crypto_sliced.columns:
        if col in maps[m]:
            vis.append(True)
        else:
            vis.append(False)
    group.append(m)
    visList.append(vis)
    vis = []
    
#Create buttons for each group
buttons = []
for i, g in enumerate(group):
    button =  dict(label=g,
                   method = 'restyle',
                    args = ['visible',visList[i]])
    buttons.append(button)

buttons = [{'label': 'all',
                 'method': 'restyle',
                 'args': ['visible', [True, True, True, True, True, True]]}] + buttons

                     

# update layout with buttons                       
fig.update_layout(
    updatemenus=[
        dict(
        type="dropdown",
        direction="down",
        buttons = buttons)
    ],
)
# buttons
fig.show()


# In[55]:


#Create a dataframe to filter out daily returns % change.
crypto_sliced_vol = crypto_new.iloc[:,[0,2,4,6,8]]
crypto_sliced_vol


# In[56]:


#Create a plot for daily returns to demonstrate volatility. 
#Build a figure for all series
fig = px.line(crypto_sliced_vol, x=crypto_sliced_vol.index, y = crypto_sliced_vol.columns,)
#Map lines/series to groups
maps = {'group 1': ['BTC Daily Returns', 'ETH Daily Returns'],
           'group 2':['TRX Daily Returns', 'XMR Daily Returns', "XLM Daily Returns"]}

#Create group and trace visibilites
group = []
vis = []
visList = []
for m in maps.keys():
    for col in crypto_sliced_vol.columns:
        if col in maps[m]:
            vis.append(True)
        else:
            vis.append(False)
    group.append(m)
    visList.append(vis)
    vis = []
    
#Create buttons for each group
buttons = []
for i, g in enumerate(group):
    button =  dict(label=g,
                   method = 'restyle',
                    args = ['visible',visList[i]])
    buttons.append(button)

buttons = [{'label': 'all',
                 'method': 'restyle',
                 'args': ['visible', [True, True, True, True, True, True]]}] + buttons

                     

# update layout with buttons                       
fig.update_layout(
    updatemenus=[
        dict(
        type="dropdown",
        direction="down",
        buttons = buttons)
    ],
)
# buttons
fig.show()


# In[ ]:





# In[ ]:




