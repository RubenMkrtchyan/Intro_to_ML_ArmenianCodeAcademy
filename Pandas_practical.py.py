#!/usr/bin/env python
# coding: utf-8

# # Practical

# ## Problem 1

# ## Importing pandas
# 
# **1.** Import pandas under the name `pd`.
# 
# Import արեք pandas մոդուլը `pd` անունով։

# In[17]:


import pandas as pd


# **2.** Print the version of pandas that has been imported.
# 
#  Տպեք pandas մոդուլի տարբերակը։

# In[18]:


pd.__version__


# ## DataFrame basics
# 
# 
# 
# Consider the following Python dictionary `data` and Python list `labels`:
# 
# 
# 

# In[19]:


import numpy as np



data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# **3.** Create a DataFrame `df` from this dictionary `data` which has the index `labels`.
# 
# Ստեղծեք `df` DataFrame `data` dictionary-ից, որի index-ը կլինի `labels` list-ը։

# In[20]:


df = pd.DataFrame(data = data, index = labels)
df


# **4.** Return the first 3 rows of the DataFrame `df`.
# 
# Տպեք `df` DataFrame-ի առաջին 3 տողերը։

# In[21]:


df.iloc[:3]


# **5.** Select just the `animal` and `age` columns from the DataFrame `df`.
# 
# `df` DataFrame-ից ընտրեք միայն `animal` և `age` սյուները։

# In[22]:


df[['animal','age']]


# **6.** Select the data in rows `[3, 4, 8]` and in columns `['animal', 'age']`.
# 
# `df`-ից վերցրեք `[3, 4, 8]` տողերում ու `['animal', 'age']` սյուներում գտնվեղ տվյալները։

# In[31]:


df[['animal','age']].iloc[[3, 4, 8]]


# **7.** Select only the rows where the number of visits is greater than 3.
# 
# Ընտրեք `df` DataFrame-ի այն տողերը, որոնց տվյալների համար visits սյան արժեքը 3-ից մեծ է։

# In[35]:


df[df['visits']>3]


# **8.** Select the rows where the age is missing, i.e. is `NaN`.
# 
# Ընտրեք այն տողերը, որոնց տվյալների համար age սյունի արժեքը բացակայում է՝ այսինքն `NaN` է։

# In[37]:


df[df['age'].isna()]


# **9.** Select the rows where the animal is a cat and the age is less than 3.
# 
# Ընտրեք այն տողերը, որոնց տվյալների համար animal սյունի արժեքը cat է և age սյունի արժեքը փոքր է 3-ից։

# In[39]:


df[(df['animal'] == 'cat') & (df['age'] < 3)]


# **10.** Change the age in row 'f' to 1.5.
# 
# Փոխարինեք 'f' տողի age սյունի արժեքը 1.5-ով։

# In[42]:


df.loc['f', 'age'] = 1.5


# **11.** Add a new column 'n' with all 1s.
# 
# Ավելացրեք միայն 1-եր պարունակող 'n' սյունը։

# In[45]:


df['n'] = '1'


# **12.** Count the number of each type of animal in `df`.
# 
# Հաշվեք `df`-ում տեղ գտած կենդանիների տիպերի քանակը։

# In[51]:


df['animal'].value_counts()


# ## Problem 2

# ### Import the library pandas as pd
# 
# #### Import արեք pandas գրադարանը pd  անունով

# In[52]:


import pandas as pd


# ### Use the dataset gender.txt, assign to a variable gender and use user_id as index
# 
# ### Օգտագործեք gender.txt dataset-ը, վերագրեք այն gender փոփոխականին ու օգտագործեք  user_id սյունը որպես index

# In[59]:


gender = pd.read_csv('gender.txt', sep = '|' , index_col = 'user_id')


# ### Print the first 20 entries
# 
# ### Տպեք առաջին 20 արժեքները

# In[60]:


gender.head(20)


# ### Print the last 10 entries
# 
# ### Տպեք վերջին 10 արժեքները

# In[61]:


gender.tail(10)


# ### What is the number of rows in the dataset?
# 
# ### Քանի տող կա dataset-ում?

# In[76]:


gender.shape[0]


# ### What is the number of columns in the dataset?
# 
# ### Քանի սյուն կա dataset-ում?

# In[75]:


gender.shape[1]


# ### Print the name of all the columns
# 
# ### Տպեք սյուների անունները

# In[78]:


gender.columns


# ### How is the dataset indexed?
# 
# ### Ինչպես է ինդեքսավորված dataset-ը?

# In[81]:


gender.index


# ### What is the data type of each column?
# 
# ### Ինչ տիպի է ամեն սյունը՞

# In[90]:


gender.dtypes


# ### Print only the occupation column
# 
# ### Տպեք միայն occupation սյունը

# In[91]:


gender['occupation']


# ### How many different occupations there are in this dataset?
# 
# ### Քանի տարբեր occupation կա dataset-ում?

# In[95]:


len(gender['occupation'].value_counts())


# ### What is the most popular occupation?
# 
# ### Որն է ամենահաճախ հանդիպող occupation-ը?

# In[108]:


gender['occupation'].mode()[0]


# ## Problem 3

# ### Import the libraries
# 
# ### Import արեք pandas գրադարանը pd անունով

# In[109]:


import pandas as pd


# ### Import the dataset drinks.csv, assign it to a variable called drinks
# 
# ### Import արեք drinks.csv dataset-ը, վերագրեք այն drinks փոփոխականին

# In[117]:


drinks = pd.read_csv('drinks.csv')


# ### Which continent drinks more beer on average?
# 
# ### Որ continent-ն է միջինում ավելի շատ գարեջուր խմում՞

# In[229]:


print(drinks.groupby('continent')['beer_servings'].mean().reset_index())
print("Based on the data, on average, population of Europe drinks more beer than others do")


# ### For each continent print the statistics for wine consumption
# 
# ### Ամեն continent-ի համար տպեք wine_servings-ի ստատիստիկան (mean, min, max, std, quartiles)

# In[233]:


drinks.groupby('continent')['wine_servings'].describe().reset_index()


# ### Print the mean alcohol consumption per continent for every column
# 
# ### Ամեն սյան համար տպեք միջին ալկոհոլի օգտագործման քանակը ամեն continent-ի համար

# In[237]:


drinks.groupby('continent').mean().reset_index()


# ### Print the median alcohol consumption per continent for every column
# 
# ### Ամեն սյան համար տպեք մեդիան ալկոհոլի օգտագործման քանակը ամեն continent-ի համար

# In[238]:


drinks.groupby('continent').median().reset_index()


# ### Print the mean, min and max values for spirt consumption. 
# 
# ### Տպեք spirt-ի օգտագործման mean, min ու max-ը։ 

# In[243]:


drinks['spirit_servings'].agg(['mean', 'min', 'max']).reset_index()

