#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1


# In[3]:


import numpy as np


# In[5]:


X = np.array([0,1,2,3,4,5,6,7,8,9])
X


# In[8]:


X = np.arange(0,10)
X


# In[ ]:


#Question 2


# In[11]:


y = np.ones(shape = (3,3), dtype = bool)
y


# In[12]:


#Question 3


# In[15]:


z = np.arange(start = 1, stop = 100,step = 2)
z


# In[16]:


z = np.arange(0,100)
z[z%2 == 1]


# In[14]:


#Question 4


# In[18]:


z[z%2 == 1] = -2
z


# In[ ]:


#Question 5/6


# In[30]:


q = np.arange(1,7)
q


# In[31]:


q = q.reshape(2,3)
q


# In[36]:


q.ndim


# In[33]:


q.dtype


# In[ ]:


#Question 7


# In[11]:


a  = np.array([1,2,3,4,5,6,7,8,9])
b = a[np.where((a%2 == 1) | (a%4 == 0))]
b


# In[ ]:


#Question 8


# In[19]:


arr = np.array([[1,2, np.nan], [4,np.nan,6]])
arr


# In[22]:


np.isnan(arr)


# In[ ]:


#Question 9


# In[24]:


np.nan_to_num(arr)


# In[ ]:


#Question 10


# In[25]:


u = np.array([[1,1,3],[4,5,5]])
u


# In[27]:


np.unique(u, return_counts = True)


# In[ ]:


#Question 11


# In[36]:


w = np.array([[1,2], [3,4]])
w


# In[37]:


w = np.array([[1,2], [3,4]], dtype='<U1')
w


# In[28]:


#Question 12


# In[45]:


y = np.arange(99,300)
y = y[((y%5 == 0) | (y%7 == 0)) != ((y%5 == 0) & (y%7 == 0))]


# In[46]:


y


# In[44]:


y = np.arange(99,300)
y = y[(y%5 == 0) & (y%7 == 0)]
y


# In[47]:


y = np.arange(99,300)
y = y[(y%5 == 0) | (y%7 == 0)]
y


# In[ ]:


#Question 13


# In[48]:


array = np.array([1,2,3,4,5])


# In[50]:


for i in range(0, len(array)):
    print(array[i])
    


# In[62]:


for i in range(len(array)-1, -1, -1):
    print(array[i])

