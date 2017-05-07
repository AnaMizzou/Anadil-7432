
# coding: utf-8

# In[23]:

import pandas as pd
df1 = pd.read_csv('campuscrime.csv')
print (df1)


# In[24]:

uni=pd.read_csv('campuscrime.csv')


# In[38]:

df1.head()


# In[25]:

uni.describe()


# In[22]:

uni.sort_values(by = "total_enr")


# In[26]:

uni.sort_values(by = "burglary")


# In[27]:

uni.sort_values(by = "murder")


# In[28]:

uni.sort_values(by = "robbery")


# In[33]:

df1.manslaughter.value_counts()


# In[35]:

df1.burglary.value_counts()


# In[36]:

df1.forcible.mean()


# In[40]:

df1.loc[:,["instname", "total_enr"]]


# In[44]:

df1.shape


# In[41]:

type(False)


# In[46]:

booleans = []
for value in df1.total_enr
    if value >= 50000
        booleans.append(True)
    else:
        booleans.append(False)


# In[ ]:



