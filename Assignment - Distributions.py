#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[ ]:


# Question 1


# In[2]:


df_titanic = pd.read_csv(r'C:\Users\Lenovo\Downloads\titanic.csv')


# In[3]:


df_titanic['Age'].value_counts()


# In[6]:


df_titanic['Age'].value_counts(normalize=True)


# In[4]:


import seaborn as sns


# In[5]:


probabilities = df_titanic['Age'].value_counts(normalize=True)    
sns.barplot(probabilities.index, probabilities.values)


# In[ ]:


# Question 2


# In[2]:


from scipy.stats import norm as norm


# In[11]:


4**0


# In[14]:


0.7**5


# In[15]:


0.7**4


# In[16]:


0.7**3


# In[17]:


0.3**2


# In[18]:


5*0.3*0.24


# In[19]:


10*0.09*0.34


# In[20]:


0.168+0.36+0.306


# In[ ]:


#Question 8


# In[4]:


norm.cdf(2.23)


# In[6]:


norm.cdf(-0.82)


# In[ ]:


#Question 2


# In[3]:


norm.cdf(1.2)


# In[4]:


1- norm.cdf(1.2)


# In[5]:


norm.cdf(0.3)


# In[7]:


norm.cdf(0.05)


# In[8]:


norm.cdf(-0.8)


# In[ ]:




