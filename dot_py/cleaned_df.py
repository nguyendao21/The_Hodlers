#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys 
import fire
import csv
import questionary
import pandas as pd 
from pathlib import Path

import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go


# In[4]:


wheat_df = pd.read_csv(
    Path("../csv_data/csv_files_agriculture/zw_wheat.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)


wheat_df = wheat_df.drop(columns=['Volume', 'Open', 'High', 'Low'])
wheat_df


# In[5]:


wheat_df = wheat_df.rename(columns={'Close/Last' : 'Wheat'})
wheat_df


# In[77]:


# Filtering my dataframes so that dates that are unused are removed.


wheat_cleaned = wheat_df.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')
wheat_cleaned.head()


# In[78]:



wheat_cleaned.dtypes


# In[7]:


corn_df = pd.read_csv(
    Path("../csv_data/csv_files_agriculture/zc_corn.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)

corn_df = corn_df.drop(columns=['Volume', 'Open', 'High', 'Low'])
corn_df


# In[8]:


corn_df = corn_df.rename(columns={'Close/Last' : 'Corn'})
corn_df


# In[81]:



# Filtering my dataframes so that dates that are unused are removed.
corn_cleaned = corn_df.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')
corn_cleaned


# In[9]:


fd_cattle_df = pd.read_csv(
    Path("../csv_data/csv_files_agriculture/fd_cattle.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)

fd_cattle_df = fd_cattle_df.drop(columns=['Volume', 'Open', 'High', 'Low'])
fd_cattle_df



# In[13]:


fd_cattle_df = fd_cattle_df.rename(columns={'Close/Last' : 'FD Cattle'})
fd_cattle_df


# In[14]:


# Filtering my dataframes so that dates that are unused are removed.
fd_cattle_cleaned = fd_cattle_df.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')
fd_cattle_cleaned.head()


# In[15]:


fd_cattle_cleaned.dtypes


# In[16]:


hogs_df = pd.read_csv(
    Path("../csv_data/csv_files_agriculture/he_hogs.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)

hogs_df = hogs_df.drop(columns=['Volume', 'Open', 'High', 'Low'])
hogs_df


# In[87]:


hogs_df = hogs_df.rename(columns={'Close/Last' : 'Hogs'})
hogs_df


# In[88]:


# Filtering my dataframes so that dates that are unused are removed.
hogs_cleaned = hogs_df.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')
hogs_cleaned


# In[89]:


hogs_cleaned.dtypes


# In[17]:


gf_cattle = pd.read_csv(
    Path("../csv_data/csv_files_agriculture/gf_cattle.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)

gf_cattle = gf_cattle.drop(columns=['Volume', 'Open', 'High', 'Low'])


# In[18]:


gf_cattle = gf_cattle.rename(columns={'Close/Last' : 'GF Cattle'})
gf_cattle


# In[19]:


# Filtering my dataframes so that dates that are unused are removed.
gf_cattle_cleaned = gf_cattle.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')
gf_cattle_cleaned


# In[93]:


# Using Concat to combine all dataframes into one

agriculture_df_closing_price = pd.concat([wheat_cleaned, corn_cleaned, fd_cattle_cleaned, hogs_cleaned, gf_cattle_cleaned], axis = 1, join = "inner")
agriculture_df_closing_price


# In[94]:


agriculture_df_daily_returns = agriculture_df_closing_price.pct_change().dropna()


# In[95]:


agriculture_df_daily_returns


# In[96]:


#define the stimulus starting amoung in var
starting_value= float(input("starting amount"))


# In[97]:


starting_value


# In[98]:


# Calculate daily returns for Wheat in a new dataframe

wheat_daily_returns = wheat_cleaned.pct_change()

wheat_daily_returns.head()


# In[99]:


wheat_daily_returns['Portfolio'] = pd.NaT

wheat_daily_returns


# In[100]:


wheat_daily_returns = wheat_daily_returns.assign(Portfolio=(1+wheat_daily_returns['Wheat'].fillna(0)).cumprod().mul(starting_value))


# In[101]:


#Rename columns. 
wheat = wheat_daily_returns.rename(columns={'Wheat':'Wheat Daily Returns',"Portfolio":"Wheat Port"})


# In[102]:


wheat.head()


# In[103]:


corn_daily_returns = corn_cleaned.pct_change()

corn_daily_returns.head()


# In[104]:


corn_daily_returns['Portfolio'] = pd.NaT

corn_daily_returns


# In[105]:


corn_daily_returns = corn_daily_returns.assign(Portfolio=(1+corn_daily_returns['Corn'].fillna(0)).cumprod().mul(starting_value))


# In[106]:


corn = corn_daily_returns.rename(columns={'Corn':'Corn Daily Returns',"Portfolio":"Corn Port"})


# In[107]:


corn.tail()


# In[108]:


fd_cattle_daily_returns = fd_cattle_cleaned.pct_change()

fd_cattle_daily_returns.head()


# In[109]:


fd_cattle_daily_returns['Portfolio'] = pd.NaT

fd_cattle_daily_returns


# In[110]:


fd_cattle_daily_returns = fd_cattle_daily_returns.assign(Portfolio=(1+fd_cattle_daily_returns['FD Cattle'].fillna(0)).cumprod().mul(starting_value))


# In[111]:


fd_cattle = fd_cattle_daily_returns.rename(columns={'FD Cattle':'FD Cattle Daily Returns',"Portfolio":"FD Cattle Port"})


# In[112]:


fd_cattle


# In[113]:


hogs_daily_returns = hogs_cleaned.pct_change()

hogs_daily_returns.head()


# In[114]:


hogs_daily_returns['Portfolio'] = pd.NaT

hogs_daily_returns


# In[115]:


hogs_daily_returns = hogs_daily_returns.assign(Portfolio=(1+hogs_daily_returns['Hogs'].fillna(0)).cumprod().mul(starting_value))


# In[116]:


hogs = hogs_daily_returns.rename(columns={'Hogs':'Hogs Daily Returns',"Portfolio":"Hogs Port"})
hogs.head()


# In[117]:


gf_cattle_daily_returns = gf_cattle_cleaned.pct_change()

gf_cattle_daily_returns.head()


# In[118]:


gf_cattle_daily_returns['Portfolio'] = pd.NaT

gf_cattle_daily_returns


# In[119]:


gf_cattle_daily_returns = gf_cattle_daily_returns.assign(Portfolio=(1+gf_cattle_daily_returns['GF Cattle'].fillna(0)).cumprod().mul(starting_value))


# In[120]:


gf_cattle = gf_cattle_daily_returns.rename(columns={'FD Cattle':'FD Cattle Daily Returns',"Portfolio":"GF Cattle Port"})
gf_cattle.head()


# In[122]:


agriculture_daily_returns = pd.concat([wheat, corn, fd_cattle, hogs, gf_cattle], axis=1)


# In[123]:


agriculture_daily_returns


# In[128]:


agriculture_daily_returns.plot()


# In[129]:


agriculture_daily_returns_sliced = agriculture_daily_returns.iloc[:, [1,3,5,7,9]]
agriculture_daily_returns_sliced


# In[ ]:




