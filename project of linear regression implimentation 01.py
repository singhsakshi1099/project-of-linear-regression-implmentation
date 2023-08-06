#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np 
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[15]:


df = pd.read_excel("l.d.xlsx")


# In[22]:


df


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df['Area'],df['price'],color='red',marker='+')


# In[26]:


new_df = df.drop('price',axis='columns')
new_df


# In[50]:


model = linear_model.LinearRegression()
model.fit(new_df, df.price)


# In[51]:


model.predict([[3300]])


# In[66]:


3300*135.78767123 + 180616.43835616432


# In[73]:


area_df = pd.read_excel("l.d.xlsx")
area_df.head(3)


# In[ ]:





# In[ ]:




