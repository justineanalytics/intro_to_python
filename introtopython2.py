#!/usr/bin/env python
# coding: utf-8

# In[1]:


1 + 1


# In[2]:


10 - 9


# In[3]:


a = 7


# In[4]:


a + 5


# In[5]:


a == 5


# In[6]:


a == 7


# In[7]:


import pandas as pd


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


import seaborn as sns


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df = pd.read_csv('https://raw.githubusercontent.com/venky14/iris-dataset/master/iris-species/Iris.csv')


# In[12]:


df.head()


# In[13]:


df.describe()


# In[15]:


df.shape


# In[17]:


df.info()


# In[18]:


df.mean()


# In[20]:


df.groupby('Species')['PetalLengthCm'].mean()


# In[23]:


df.groupby('Species')['SepalWidthCm'].min()


# In[24]:


df[df['SepalWidthCm'] > 3.5 ]['PetalLengthCm'].mean()


# In[26]:


sns.scatterplot(x='PetalLengthCm', y='SepalLengthCm', data=df, hue='Species')


# In[28]:


sns.pairplot(df);


# In[29]:


df.sort_values("SepalWidthCm").head()


# In[30]:


df.sort_values("SepalWidthCm",ascending=False).head()


# In[31]:


df.head()


# In[39]:


df2 = df.sort_values("SepalWidthCm",ascending=False)


# In[40]:


df2.head()


# In[41]:


df2.to_csv(r'C:\Users\justine.braun\Desktop\Python\df2.csv', index=False)


# In[ ]:




