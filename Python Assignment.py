#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##QUESTIONS ON STRINGS -------------------------------


# In[15]:


string_old = "I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"


# In[2]:


len(string)


# In[3]:


string.lower()


# In[10]:


# importing a string of punctuation and digits to remove
import string
exclist = string.punctuation 
# remove punctuations and digits from oldtext
table_ = str.maketrans('', '', exclist)
newtext = string_old.translate(table_)


# In[9]:


newtext


# In[12]:


import re


# In[16]:


res = re.sub(r'[^\w\s]', '', string_old) 


# In[17]:


res


# In[18]:


newtext.find('Data Science')


# In[23]:


newtext[43:55]


# In[24]:


from collections import Counter


# In[25]:


freq = Counter(newtext.split()).most_common()


# In[26]:


print(freq)


# In[27]:


newtext.replace('Supervised', "Unsupervised")


# In[28]:


string_old.split('.')


# In[29]:


string_old.endswith('e')


# In[65]:


list = re.findall("['e'$]", string_old)


# In[66]:


list


# In[ ]:





# In[ ]:





# In[ ]:


## Questions on Dictionary ----------------------


# In[96]:


dict = {'Apple': '250g', 'Sugar': '500g', 'Rice': '2.5Kg', 'Milk':'2.5lt', 'Eggs': '1 Dozen'}


# In[97]:


dict.update({'Wheat' : '1Kg'})


# In[98]:


dict


# In[99]:


dict['Rice']='1 Kg'


# In[100]:


dict


# In[82]:


dict_items = dict.items()


# In[85]:


for items in dict.items():
    print(items)


# In[111]:


dict_p = {'Apple' : 220, 'Sugar' : 43, 'Rice' : 45, 'Milk' : 30, 'Eggs': 60}


# In[112]:


dict_Org = {'Apple': 250/1000, 'Sugar': 500/1000, 'Rice': 2.5, 'Milk':2.5, 'Eggs': 1}


# In[113]:


{k: dict_Org[k]*dict_p[k] for k in dict_Org}


# In[ ]:


# QUESTIONS ON LISTS -----------------------


# In[6]:


AI_Companies = ['Amazon', 'Facebook', 'HiSilicon', 'Google', 'Apple', 'Microsoft', 'SenseTime']


# In[2]:


AI_Companies.sort()


# In[3]:


AI_Companies


# In[10]:


AI_Companies.extend(['Nvidia', 'OpenAI', 'Qualcomm', 'Reliance'])


# In[11]:


AI_Companies


# In[12]:


AI_Companies.remove('Reliance')


# In[14]:


AI_Companies


# In[25]:


AI_Companies[2:6]


# In[ ]:


## Questions on Tuple-----------------------


# In[2]:


dict_p = (220, 43, 45, 30, 60)


# In[3]:


max(dict_p)


# In[4]:


min(dict_p)


# In[13]:


AI_Companies = tuple(AI_Companies)
AI_Companies


# In[10]:


dict_p + AI_Companies


# In[11]:


len(dict_p)


# In[12]:


len(AI_Companies)

