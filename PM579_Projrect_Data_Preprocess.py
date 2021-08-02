#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd 
# Read in dataframe 
df1 = pd.read_excel('data/plasma.xlsx', index_col=0)
df1


# In[25]:


# Subset the dataframe based on treatment condition
df_after = df1[df1["treat"] == 1 ]
df_before = df1[df1["treat"] == 0 ]
# merge two dataframe based on ID
df_result = pd.merge(df_before, df_after, on='ID', suffixes = ('_before', '_after'))
df_result.head()


# In[26]:


# export dataframe to excel
df_result.to_excel("plasma_reform.xlsx")


# In[ ]:




