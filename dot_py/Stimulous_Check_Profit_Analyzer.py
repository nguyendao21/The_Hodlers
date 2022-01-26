#!/usr/bin/env python
# coding: utf-8

# # Stimulous Check Profit Analyzer

# In[2]:


# Import the required libraries and dependencies.
import sys 
import fire
import csv
import numpy as np
import questionary
import pandas as pd 
from pathlib import Path
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go


# In[3]:


# Read in the CSV file called "Resources.csv" using the Path module.
# The CSV file is located int the Stimulous_Check_Profit_Analyzer folder.
# Set the index to the column "Date".
# Set the parse_date and infer_datetime_format parameters.
gold_df = pd.read_csv(
    Path('../csv_data/csv_files_resources/gold.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)

# Verify 'Gold' data-type as "float."
gold_df.dtypes


# In[4]:


# Filter out 'Gold Close' price into a sliced dataframe. 
gold_sliced = gold_df.iloc[:,[0]]

#Rename 'close' price to 'Gold' in a new dataframe.
gold_new = gold_sliced.rename(columns={"Price":'Gold'})

# View the first 5 rows of the DataFrame.
gold_new.head()


# In[12]:


silver_df = pd.read_csv(
    Path('../csv_data/csv_files_resources/silver.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)

# Verify 'Silver' data-type as "float."
silver_df.dtypes


# In[13]:


# Filter out 'Silver Close' price into a sliced dataframe. 
silver_sliced = silver_df.iloc[:,[0]]

#Rename 'close' price to 'Silver' in a new dataframe.
silver_new = silver_sliced.rename(columns={"Price":'Silver'})

# View the first 5 rows of the DataFrame.
silver_new.head()


# In[14]:


crude_oil_df = pd.read_csv(
    Path('../csv_data/csv_files_resources/crude_oil.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)

# Verify 'Crude Oil' data-type as "float."
crude_oil_df.dtypes


# In[15]:


# Filter out 'Crude Oil Close' price into a sliced dataframe. 
crude_oil_sliced = crude_oil_df.iloc[:,[0]]

#Rename 'close' price to 'Crude Oil' in a new dataframe.
crude_oil_new = crude_oil_sliced.rename(columns={"Price":'Crude Oil'})

# View the first 5 rows of the DataFrame.
crude_oil_new.head()


# In[16]:


lumber_df = pd.read_csv(
    Path('../csv_data/csv_files_resources/lumber.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)

# Verify 'Lumber' data-type as "float."
lumber_df.dtypes


# In[17]:


# Filter out 'Lumber Close' price into a sliced dataframe. 
lumber_sliced = lumber_df.iloc[:,[0]]

#Rename 'close' price to 'Lumber' in a new dataframe.
lumber_new = lumber_sliced.rename(columns={"Price":'Lumber'})

# View the first 5 rows of the DataFrame.
lumber_new.head()


# In[18]:


gasoline_df = pd.read_csv(
    Path('../csv_data/csv_files_resources/gasoline.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)

# Verify 'Gasoline' data-type as "float."
gasoline_df.dtypes


# In[19]:


# Filter out 'Gasoline Close' price into a sliced dataframe. 
gasoline_sliced = gasoline_df.iloc[:,[0]]

#Rename 'close' price to 'Lumber' in a new dataframe.
gasoline_new = gasoline_sliced.rename(columns={"Price":'Gasoline'})

# View the first 5 rows of the DataFrame.
gasoline_new.head()


# In[104]:


# Use concatenate function to group btc_new, eth_new, trx_new, xlm_new, xmr_new dataframes into a single dataframe called 'resources'.
resources = pd.concat([gold_new, silver_new, crude_oil_new, lumber_new, gasoline_new], axis=1)
# Display results. 
resources


# In[105]:


resources_daily_returns = resources.pct_change()
resources_daily_returns.head()


# In[106]:


#Define the stimulus amount in a new variable.
starting_value = float(input("Starting amount"))


# In[107]:


starting_value


# In[112]:


#Calculate daily returns for Gold in a new dataframe. 
gold_daily_returns = gold_new.pct_change()

gold_daily_returns.head()


# In[113]:


#Add an empty portfolio column to Gold Daily Returns. 
gold_daily_returns['Portfolio'] = pd.NaT

gold_daily_returns


# In[125]:


#Calculate the portfolio value over time. 
gold_daily_returns = gold_daily_returns.assign(Portfolio=(1+gold_daily_returns['Gold'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
gold = gold_daily_returns.rename(columns={'Gold':'Gold Daily Returns', "Portfolio":" Gold Port"})

#Display results. 
gold.head()


# In[114]:


#Calculate daily returns for Silver in a new dataframe. 
silver_daily_returns = silver_new.pct_change()

silver_daily_returns.head()


# In[115]:


#Add an empty portfolio column to Silver Daily Returns. 
silver_daily_returns['Portfolio'] = pd.NaT

silver_daily_returns


# In[126]:


#Calculate the portfolio value over time. 
silver_daily_returns = silver_daily_returns.assign(Portfolio=(1+silver_daily_returns['Silver'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
silver = silver_daily_returns.rename(columns={'Silver':'Silver Daily Returns', "Portfolio":" Silver Port"})

#Display results. 
silver.head()


# In[119]:


#Calculate daily returns for Crude Oil in a new dataframe. 
crude_oil_daily_returns = crude_oil_new.pct_change()

crude_oil_daily_returns.head()


# In[120]:


#Add an empty portfolio column to Crude Oil Daily Returns. 
crude_oil_daily_returns['Portfolio'] = pd.NaT

crude_oil_daily_returns


# In[128]:


#Calculate the portfolio value over time. 
crude_oil_daily_returns = crude_oil_daily_returns.assign(Portfolio=(1+crude_oil_daily_returns['Crude Oil'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
crude_oil = crude_oil_daily_returns.rename(columns={'Crude Oil':'Crude Oil Daily Returns', "Portfolio": "Crude Oil Port"})

#Display results. 
crude_oil.head()


# In[121]:


#Calculate daily returns for Lumber in a new dataframe. 
lumber_daily_returns = lumber_new.pct_change()

lumber_daily_returns.head()


# In[122]:


#Add an empty portfolio column to Lumber Daily Returns. 
lumber_daily_returns['Portfolio'] = pd.NaT

lumber_daily_returns


# In[130]:


#Calculate the portfolio value over time. 
lumber_daily_returns = lumber_daily_returns.assign(Portfolio=(1+lumber_daily_returns['Lumber'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
lumber = lumber_daily_returns.rename(columns={'Lumber':'Lumber Daily Returns', "Portfolio": "Lumber Port"})

#Display results. 
lumber.head()


# In[123]:


#Calculate daily returns for Gasoline in a new dataframe. 
gasoline_daily_returns = gasoline_new.pct_change()

gasoline_daily_returns.head()


# In[124]:


#Add an empty portfolio column to Gasoline Daily Returns. 
gasoline_daily_returns['Portfolio'] = pd.NaT

gasoline_daily_returns


# In[131]:


#Calculate the portfolio value over time. 
gasoline_daily_returns = gasoline_daily_returns.assign(Portfolio=(1+gasoline_daily_returns['Gasoline'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
gasoline = gasoline_daily_returns.rename(columns={'Gasoline':'Gasoline Daily Returns', "Portfolio":" Gasoline Port"})

#Display results. 
gasoline.head()


# In[136]:


#Use concatenate function to group the daily_returns and port values into one dataframe. 
resources_new = pd.concat([gold, silver, crude_oil, lumber, gasoline],axis=1)

#Display results.
resources_new


# In[137]:


resources_new.plot()


# In[138]:


#Drop 'Daily Returns' column. 
resources_sliced = resources_new.iloc[:,[1,3,5,7,9]]
resources_sliced


# In[140]:


#Build a figure for all series
fig = px.line(resources_sliced, x=resources_sliced.index, y = resources_sliced.columns)
#Map lines/series to groups
maps = {'group 1': ['Gold Port', 'Silver Port'],
           'group 2':['Crude Oil Port', 'Lumber Port', "Gasoline Port"]}

#Create group and trace visibilites
group = []
vis = []
visList = []
for m in maps.keys():
    for col in resources_sliced.columns:
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


# In[141]:


#Create a dataframe to filter out daily returns % change.
resources_sliced_vol = resources_new.iloc[:,[0,2,4,6,8]]
resources_sliced_vol


# In[142]:


#Create a plot for daily returns to demonstrate volatility. 
#Build a figure for all series
fig = px.line(resources_sliced_vol, x=resources_sliced_vol.index, y = resources_sliced_vol.columns,)
#Map lines/series to groups
maps = {'group 1': ['Gold Daily Returns', 'Silver Daily Returns'],
           'group 2':['Crude Oil Daily Returns', 'Lumber Daily Returns', "Gasoline Daily Returns"]}

#Create group and trace visibilites
group = []
vis = []
visList = []
for m in maps.keys():
    for col in resources_sliced_vol.columns:
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





# In[ ]:





# In[ ]:




