#!/usr/bin/env python
# coding: utf-8

# # Homework

# ## Problem 4

# ### Import the libraries
# 
# #### Import արեք pandas գրադարանը pd  անունով

# In[1]:


import pandas as pd


# ### Import the dataset baby_names.txt, assign it to a variable called baby_names
# 
# ### Import արեք baby_names.txt dataset-ը ու այն վերագրեք baby_names փոփոխականի

# In[2]:


baby_names = pd.read_csv('baby_names.csv')
baby_names


# ### See the first 10 entries.
# 
# ### Տպեք առաջին 10 արժեքը

# In[3]:


baby_names.head(10)


# ### Delete the columns 'Unnamed: 0' and 'Id'
# 
# ### Ջնջեք 'Unnamed: 0' ու 'Id' սյուները

# In[8]:


baby_names.drop(columns = ['Unnamed: 0', 'Id'], inplace = True)


# ### Are there more male or female names in the dataset?
# 
# ### Արդյոք dataset-ում ավելի շատ են կանացի թե տղամարդու անունները?

# In[76]:


print(baby_names['Gender'].value_counts())
print("\nFemales are the majority")


# ### Delete the column 'Year'. Group the dataset by name and assign to names.
# 
# ### Ջնջեք 'Year' սյունը. Խմբավորեք dataset-ը ըստ անունի ու վերագրեք արդյունքը names փոփոխականին

# In[22]:


baby_names.drop(columns = ['Year'], inplace = True)
names = baby_names.groupby('Name')


# ### How many different names exist in the dataset?
# 
# ### Քանի հատ տարբեր անուն կա dataset-ում?

# In[45]:


names.nunique().shape[0]


# ### What is the name with most occurrences?
# 
# ### Որն է ամենաշատ հանդիպող անունը?

# In[78]:


print(baby_names["Name"].value_counts().head(1))
print("\nThe name with most occurrences is Riley")


# ### What is the median name occurrence?
# 
# ### Որն է անունների հանդիպման մեդիանը՞ 

# In[73]:


baby_names["Name"].value_counts().median()


# ### Get a summary with the mean, min, max, std and quartiles.
# 
# ### Ստացեք dataset-ի ամփոփում mean, min, max, std ու quartile-ներով

# In[66]:


baby_names.describe()

