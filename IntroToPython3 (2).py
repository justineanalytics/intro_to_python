#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


import csv


# In[5]:


import os


# In[6]:


os.getcwd()


# In[7]:


cd /Users/justine.braun/Desktop/Python


# In[8]:


df = pd.read_csv('df.csv')


# In[9]:


df.head()


# In[10]:


df.dtypes


# In[11]:


df = df.rename(columns={'Published Date': 'Date'})


# In[12]:


df.head()


# In[13]:


df['Date'] = pd.to_datetime(df['Date'], utc=True)


# In[14]:


df.dtypes


# In[15]:


df['Month'] = pd.DatetimeIndex(df['Date']).month


# In[16]:


df.head()


# In[17]:


df['TW_Engagements'] = df['Twitter - Post Replies'] + df['Twitter - Post Native Retweets'] + df['Twitter - Post Likes']


# In[18]:


df['IG_Engagements'] = df['Instagram - Post Likes'] + df['Instagram - Post Comments']


# In[19]:


df['IGS_Engagements'] = df['Instagram - Story Taps Back'] + df['Instagram - Story Replies']


# In[20]:


df = df.rename(columns={'Instagram - Story Impressions': 'Instagram_Story_Impressions'})


# In[21]:


df.head()


# In[22]:


df['Channel'] = np.where((df.Instagram_Story_Impressions > 0), "IGS", df.Channel)


# In[23]:


df.head()


# In[24]:


df['Engagements'] = df['TW_Engagements'] + df['IG_Engagements'] + df['IGS_Engagements']


# In[25]:


df['Impressions'] = df['Instagram_Story_Impressions'] + df['Instagram - Post Impressions'] + df['Twitter - Post Impressions - Advanced']


# In[ ]:





# In[26]:


df2 = df[(df['Impressions'] > 0)]


# In[27]:


df.shape


# In[28]:


df2.shape


# In[29]:


print(df.groupby(['Channel', 'Month']).mean())     # Get mean across variables by subgroups


# In[30]:


df.groupby('Channel')['Engagements'].mean()


# In[31]:


df.groupby('Channel')['Impressions'].mean()


# In[32]:


df.groupby('Month')['Engagements'].mean()


# In[33]:


df.groupby('Month')['Impressions'].mean()


# In[34]:


df.groupby(['Channel', 'Month'])['Engagements'].mean()


# In[35]:


df.groupby(['Channel', 'Month'])['Impressions'].mean()


# In[36]:


df['ER'] = df['Engagements'] / df['Impressions']


# In[37]:


df.groupby(['Channel', 'Month'])['ER'].mean()


# In[38]:


Engagements = df.groupby(['Channel', 'Month'])['Engagements'].mean()


# In[39]:


Engagements.to_csv(r'C:\Users\justine.braun\Desktop\Python\Engagements.csv', index=False)


# In[ ]:




