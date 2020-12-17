#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt


# In[2]:


import matplotlib
matplotlib._version_


# In[5]:


import numpy
numpy._version_


# In[17]:


import numpy as np
import pandas as pd
import matplotlib.colors 
import seaborn as sns


# In[7]:


plt.plot([1,2,3], [4,5,6])


# In[10]:


x = [3.4, 4.5, 6.7]
y = [7.9,3.8,8.8]
plt.plot(x,y) 
plt.show() # To remove the object line which comes from writing the plt.plot function


# In[11]:


plt.plot([1,2,3],[4,5,6], '--')


# In[14]:


plt.scatter([1,2,3],[4,5,6], marker = '+') #Once I write one code and get one canvas all plots will be 
#created in the same canvas
plt.plot([9,8,5],[0,-2,-4]) 
#This is called as OverLay


# In[24]:


iris = pd.read_csv(r'D:\Supervised Learning  - Course\end to end data sets\iris.csv')


# In[25]:


iris.head()


# In[31]:


plt.scatter(iris['Sepal.Length'], iris['Sepal.Width'])


# In[33]:


# seed the random number generator to keep results reproducible
np.random.seed(123)

# Generate 10 random nos around 2 as x-coordinates of first data series
x0 = np.random.rand(10)+1.5

# Generate the y-coordinates another data series similarly
np.random.seed(321) 
y0 = np.random.rand(10)+2

# Generate the y-coordinates another data series similarly
np.random.seed(456)
x1 = np.random.rand(10)+2.5

np.random.seed(789)
y1 = np.random.rand(10)+2

plt.scatter(x0,y0, c='b') #specifying the colors if you don't like the default colors
plt.scatter(x1,y1, c='r')

plt.show()


# In[34]:


x = list(range(10))
y = x + np.random.rand(10)- 0.5

fit = np.polyfit(x,y,1)
np.polyfit
yfit = [n*fit[0] for n in x] + fit[1]
plt.scatter(x,y)
plt.plot(yfit, 'black')

plt.show()


# In[43]:


plt.scatter(iris['Sepal.Length'], iris['Sepal.Width'])
plt.xlabel('Sepal.Length',size=8,fontweight='semibold')
plt.ylabel('Sepal.Width',size=8,fontweight='semibold')
plt.title('sepal length vs width')


# In[ ]:


import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()

i = pd.DataFrame(data=iris['data'],columns=iris.feature_names)


# In[44]:


crop_prod = pd.read_csv('D:\Supervised Learning  - Course\end to end data sets\OECD-THND_TONNES.txt',
                        delimiter='\t')


# In[47]:


crop_prod.head(5)


# In[50]:


crop_prod.info()


# In[55]:


crop_prod.Crop.unique()


# In[56]:


crop_prod.Year.unique()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




