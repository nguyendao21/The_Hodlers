#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Import the required libraries and dependencies.
import pandas as pd
from pathlib import Path
get_ipython().run_line_magic('matplotlib', 'inline')
# Import the NumPy library
import numpy as np
import csv
import questionary
import fire
import sys
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go


# In[24]:


# Read in the CSV file called "AMC_.csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
AMC_df = pd.read_csv(
    Path('../csv_data/csv_files_stocks/AMC_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[25]:


# Preview AMC_df file
AMC_df.head()


# In[26]:


# For the AMC_df, replace or drop all NaNs or missing values in the DataFrame
AMC_df.dropna()


# In[27]:


# Convert the Close data type to a float
AMC_df.loc[:,"Close"] = AMC_df.loc[:,"Close"].astype("float")
AMC_df.dtypes


# In[28]:


#Review the data for duplicated values, and drop them if necessary.
AMC_df.drop_duplicates()


# In[29]:


# Use loc or iloc to select `Date (the index)` and `Close` from bitstamp DataFrame
AMC_sliced = AMC_df.iloc[:,[3]]
# Review the first 5 rows of DataFrame
AMC_sliced.head()


# In[30]:


# Reivew the last 5 rows 
AMC_sliced.tail()


# In[31]:


# Rename colummn Close to AMC 
AMC_new = AMC_sliced.rename(columns={"Close":"AMC"})
# Display the result
AMC_new


# In[32]:


# Read in the CSV file called "GME_.csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
GME_df = pd.read_csv(
    Path('../csv_data/csv_files_stocks/GME_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[33]:


GME_df.head()


# In[34]:


GME_df.dropna()


# In[35]:


# Convert the Close data type to a float
GME_df.loc[:,"Close"] = GME_df.loc[:,"Close"].astype("float")
GME_df.dtypes


# In[36]:


#Review the data for duplicated values, and drop them if necessary.
GME_df.drop_duplicates()


# In[37]:


# Use loc or iloc to select `Date (the index)` and `Close` from GME DataFrame
GME_sliced = GME_df.iloc[:,[3]]
# Review the first 5 rows of DataFrame
GME_sliced.head()


# In[38]:


# Review the last 5 rows of DataFrame
GME_sliced.tail()


# In[39]:


# Rename colummn Close to AMC 
GME_new = GME_sliced.rename(columns={"Close":"GME"})
# Display the result
GME_new


# In[40]:


# Using concat function to merge AMC and GME into one DataFrame
result = pd.concat([AMC_new,GME_new], axis = 1)
result


# In[41]:


# Read in the CSV file called "MSTR_csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
MSTR_df = pd.read_csv(
    Path('../csv_data/csv_files_stocks/MSTR_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[42]:


# Review the MSTR_df
MSTR_df


# In[43]:


# Convert the Close data type to a float
MSTR_df.loc[:,"Close"] = MSTR_df.loc[:,"Close"].astype("float")
MSTR_df.dtypes


# In[44]:


# Use loc or iloc to select `Date (the index)` and `Close` from bitstamp DataFrame
MSTR_sliced = MSTR_df.iloc[:,[3]]
# Review the DataFrame
MSTR_sliced


# In[45]:


# Rename colummn Close to MSTR
MSTR_new = MSTR_sliced.rename(columns={"Close":"MSTR"})
# Display the result
MSTR_new


# In[46]:


# Using concat function to merge AMC,GME, MSTR into one DataFrame
result = pd.concat([AMC_new,GME_new, MSTR_new], axis = 1)
result


# In[47]:


# Read in the CSV file called "SPY_csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
SPY_df = pd.read_csv(
    Path('../csv_data/csv_files_stocks/SPY_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[48]:


# Review the SPY_df
SPY_df


# In[49]:


# Convert the Close data type to a float
SPY_df.loc[:,"Close"] = SPY_df.loc[:,"Close"].astype("float")
SPY_df.dtypes


# In[50]:


# Use loc or iloc to select `Date (the index)` and `Close` from DataFrame
SPY_sliced = SPY_df.iloc[:,[3]]
# Review the DataFrame
SPY_sliced


# In[51]:


# Rename colummn Close to SPY
SPY_new = SPY_sliced.rename(columns={"Close":"SPY"})
# Display the result
SPY_new


# In[52]:


# Using concat function to merge AMC,GME, MSTR, SPY into one DataFrame
result = pd.concat([AMC_new,GME_new, MSTR_new, SPY_new], axis = 1, join = 'inner')
result


# In[53]:


# Read in the CSV file called "TSLA_csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
TSLA_df = pd.read_csv(
    Path('../csv_data/csv_files_stocks/TSLA_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[54]:


# Review the TSLAdf
TSLA_df


# In[55]:


# Convert the Close data type to a float
TSLA_df.loc[:,"Close"] = TSLA_df.loc[:,"Close"].astype("float")
TSLA_df.dtypes


# In[56]:


# Use loc or iloc to select `Date (the index)` and `Close` from DataFrame
TSLA_sliced = TSLA_df.iloc[:,[3]]
# Review the DataFrame
TSLA_sliced


# In[57]:


# Rename colummn Close to TSLA
TSLA_new = TSLA_sliced.rename(columns={"Close":"TSLA"})
# Display the result
TSLA_new


# In[58]:


# Using concat function to merge AMC,GME, MSTR, SPY and TSLA into one DataFrame
result_df = pd.concat([AMC_new,GME_new, MSTR_new, SPY_new,TSLA_new], axis = 1, join = 'inner')
result_df


# In[59]:


# Check to see if all the data is in "float"
result_df.dtypes


# In[60]:


# Calculate the daily returns each stocks in result_df DataFrame
stocks_daily_return = result_df.pct_change().dropna()
# Review 
stocks_daily_return


# In[ ]:


# Create a float input value for choosen stimulus amount
starting_value = float(input("Starting amount"))


# In[71]:


# Create a daily return for AMC in a new dataframe
AMC_daily_returns = AMC_new.pct_change()
# Review AMC daily returns
AMC_daily_returns



# In[72]:


# Add an empty "Portfolio" column for AMC_daily_returns in order
# to keep tracking the AMC cumulative return with types as NaT(represent missing value) DataFrame
AMC_daily_returns['Portfolio'] = pd.NaT
AMC_daily_returns


# In[73]:


# Calculate the AMC cumulative value over time 
AMC_daily_returns = AMC_daily_returns.assign(Portfolio=(1+AMC_daily_returns['AMC'].fillna(0)).cumprod().mul(starting_value))


# In[74]:


# Review 
AMC_daily_returns


# In[75]:


#Rename columns. 
AMC = AMC_daily_returns.rename(columns={'AMC':'AMC Daily Returns',"Portfolio":"AMC Port "})
# Review AMC Data Frame
AMC


# In[76]:


# Create a daily return for GME in a new dataframe
GME_daily_returns = GME_new.pct_change()
# Review AMC daily returns
GME_daily_returns


# In[77]:


# Add an empty "Portfolio" column for GME_daily_returns in order
# to keep tracking the AMC cumulative return with types as NaT(represent missing value) DataFrame
GME_daily_returns['Portfolio'] = pd.NaT
GME_daily_returns


# In[78]:


# Calculate the GME cumulative value over time 
GME_daily_returns = GME_daily_returns.assign(Portfolio=(1+GME_daily_returns['GME'].fillna(0)).cumprod().mul(starting_value))
# Review GME_daily_returns
GME_daily_returns 


# In[79]:


#Rename columns. 
GME = GME_daily_returns.rename(columns={'GME':'GME Daily Returns',"Portfolio":"GME Port "})
# Review GME Data Frame
GME


# In[80]:


# Create a daily return for MSTR in a new dataframe
MSTR_daily_returns = MSTR_new.pct_change()
# Review AMC daily returns
MSTR_daily_returns


# In[81]:


# Add an empty "Portfolio" column for MSTR_daily_returns in order
# to keep tracking the MSTR cumulative return with types as NaT(represent missing value) DataFrame
MSTR_daily_returns['Portfolio'] = pd.NaT
MSTR_daily_returns


# In[82]:


# Calculate the MSTR cumulative value over time 
MSTR_daily_returns = MSTR_daily_returns.assign(Portfolio=(1+MSTR_daily_returns['MSTR'].fillna(0)).cumprod().mul(starting_value))
# Review GME_daily_returns
MSTR_daily_returns 


# In[83]:


#Rename columns. 
MSTR = MSTR_daily_returns.rename(columns={'MSTR':'MSTR Daily Returns',"Portfolio":"MSTR Port "})
# Review MSTR Data Frame
MSTR


# In[84]:


# Create a daily return for SPY in a new dataframe
SPY_daily_returns = SPY_new.pct_change()
# Review AMC daily returns
SPY_daily_returns


# In[85]:


# Add an empty "Portfolio" column for MSTR_daily_returns in order
# to keep tracking the MSTR cumulative return with types as NaT(represent missing value) DataFrame
SPY_daily_returns['Portfolio'] = pd.NaT
SPY_daily_returns


# In[86]:


# Calculate the SPY cumulative value over time 
SPY_daily_returns = SPY_daily_returns.assign(Portfolio=(1+SPY_daily_returns['SPY'].fillna(0)).cumprod().mul(starting_value))
# Review GME_daily_returns
SPY_daily_returns 


# In[87]:


#Rename columns. 
SPY = SPY_daily_returns.rename(columns={'SPY':'SPY Daily Returns',"Portfolio":"SPY Port "})
# Review MSTR Data Frame
SPY


# In[88]:


# Create a daily return for TSLA in a new dataframe
TSLA_daily_returns = TSLA_new.pct_change()
# Review AMC daily returns
TSLA_daily_returns


# In[89]:


# Add an empty "Portfolio" column for TSLA_daily_returns in order
# to keep tracking the TSLA cumulative return with types as NaT(represent missing value) DataFrame
TSLA_daily_returns['Portfolio'] = pd.NaT
TSLA_daily_returns


# In[90]:


# Calculate the TSLA cumulative value over time 
TSLA_daily_returns = TSLA_daily_returns.assign(Portfolio=(1+TSLA_daily_returns['TSLA'].fillna(0)).cumprod().mul(starting_value))
# Review GME_daily_returns
TSLA_daily_returns 


# In[91]:


#Rename columns. 
TSLA = TSLA_daily_returns.rename(columns={'TSLA':'TSLA Daily Returns',"Portfolio":"TSLA Port "})
# Review TSLA Data Frame
TSLA


# In[94]:


#Use concatenate function to group the daily_returns and port values into one dataframe. 
stocks_new = pd.concat([AMC, GME, MSTR, SPY, TSLA],axis=1, join ='inner')
# Review stocks_new
stocks_new


# In[95]:


stocks_new.plot()


# In[96]:


#Drop 'Daily Returns' column. 
stocks_sliced = stocks_new.iloc[:,[1,3,5,7,9]]
stocks_sliced


# In[101]:


#Build a figure for all series
fig = px.line(stocks_sliced, x=stocks_sliced.index, y = stocks_sliced.columns, labels = {'variable': 'Portfolio Return', 'value': 'Price'})
#Map lines/series to groups
maps = {'group 1': ['AMC Port', 'SPY Port'],
           'group 2':['TSLA Port', 'MSTR Port', "GME Port"]}

#Create group and trace visibilites
group = []
vis = []
visList = []
for m in maps.keys():
    for col in stocks_sliced.columns:
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




