#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# In[4]:


data = pd.read_csv('laptop_prices.csv')


# In[5]:


data.head()


# In[7]:


data.shape


# In[8]:


data.info()


# In[9]:


data.isnull().sum()


# In[10]:


data.describe()


# In[11]:


data['Company'].value_counts().plot(kind='bar')


# In[12]:


data['OS'].value_counts().plot(kind='bar')


# In[19]:


data['Touchscreen'].value_counts().plot(kind='pie',autopct = '%.2f%%',
title = 'TouchScreen')


# In[17]:


data['Ram'].value_counts().plot(kind='bar')


# In[20]:


data['CPU_company'].value_counts().plot(kind='pie',autopct = '%.2f%%',title = 'CPU_company' )


# In[21]:


data['GPU_company'].value_counts().plot(kind='pie',autopct = '%.2f%%',title = 'GPU_company')


# In[22]:


data['IPSpanel'].value_counts().plot(kind = 'pie' , autopct = '%.f%%')


# In[23]:


data['Inches'].value_counts().plot(kind = 'bar')


# In[24]:


data['PrimaryStorageType'].value_counts().plot(kind = 'pie' , autopct =
'%.2f%%')


# In[25]:


data['Screen'].value_counts().plot(kind = 'bar')


# In[26]:


data['SecondaryStorageType'].value_counts().plot(kind = 'bar')


# In[27]:


data.info()


# In[28]:


plt.figure(figsize = (10,8))
sns.boxplot(x = data['OS'], y= data['Price_euros'])
plt.title('OS VS CPU_freqency')
plt.show()


# In[29]:


plt.figure(figsize = (10,8))
sns.barplot(x = data['Touchscreen'], y= data['Price_euros'] , hue =
data['Screen'])
plt.show()


# In[30]:


plt.figure(figsize = (10,8))
sns.barplot(x = data['OS'], y= data['Price_euros'] , hue =
data['Touchscreen'])
plt.show()


# In[31]:


plt.figure(figsize = (10,8))
sns.barplot(x = data['PrimaryStorage'], y= data['Price_euros'] , hue =
data['SecondaryStorage'])
plt.show()


# In[32]:


plt.figure(figsize = (10,8))
sns.barplot(x = data['RetinaDisplay'], y= data['Price_euros'], hue =
data['PrimaryStorage'])
plt.show()


# In[33]:


sns.scatterplot(data = data , x= data['CPU_freq'], y = data['Ram'], hue =
data['OS'])


# In[34]:


sns.scatterplot(data = data , x= data['CPU_freq'], y = data['Ram'], hue =
data['OS'])


# In[ ]:




