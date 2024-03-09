#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("cereal.csv")


# In[2]:


df


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.dtypes


# In[6]:


df.rename(columns={'mfr':'manufacturer'},inplace =True)


# In[7]:


df


# In[8]:


df.rename(columns={'protein': 'protein (g)', 'fat': 'fat (g)','sodium': 'sodium (mg)','fiber':'fiber (g)','carbo':'carbohydrates (g)','sugars':'sugars (g)','potass':'potassium (mg)','vitamins': 'vitamins %', 'weight':'weight (oz/serv)','cups': 'cups/serv'},inplace =True)
df.head()


# In[9]:


df['type']= df['type'].replace({'C':'Cold','H':'Hot'})
df.head()


# In[11]:


df['manufacturer'] = df['manufacturer'].replace({'A':'American Home Food Products','G':'General Mills','K' : 'Kelloggs','N' : 'Nabisco','P' : 'Post','Q' : 'Quaker Oats', 'R' : 'Ralston Purina'})
df.head()


# In[18]:


# to see which cereal has highest calories
highest_calories = df.sort_values(by = 'calories', ascending = False)
top10 = highest_calories.head(10)


# In[20]:


top10.head()


# In[22]:


less_calories = df.sort_values(by = 'calories', ascending = True)
less_10 = less_calories.head(10)
less_10.head()


# In[26]:


nutrients = df[['protein (g)','fat (g)', 'carbohydrates (g)', 'sugars (g)', 'fiber (g)']]
correlation = nutrients.corr()
print(correlation)


# In[27]:


plt.figure(figsize=(10,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm',fmt=".2f")
plt.title('Matrix Correlation Between Nutrients')
plt.show()


# In[50]:


df.dropna()
df.head()


# In[ ]:




