#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Load dataset
df1= pd.read_csv(r'C:\Users\Shiva Murthy\Downloads\SRI\Data Analytics\Trainity\6. Bank Loan Case Study\previous_application.csv')
df2= pd.read_csv(r'C:\Users\Shiva Murthy\Downloads\SRI\Data Analytics\Trainity\6. Bank Loan Case Study\application_data.csv')


# In[ ]:


# Data Exploration


# In[3]:


df1.shape


# In[4]:


df2.shape


# In[18]:


df1


# In[19]:


df2


# In[ ]:


# Data Cleaning


# In[6]:


# Checking for duplicate values(df1)
duplicate = df1[df1.duplicated()]
 
print("Duplicate Rows :")
 
# Print the resultant Dataframe
duplicate


# In[8]:


# Checking for duplicate values(df2)
duplicate = df2[df2.duplicated()]
 
print("Duplicate Rows :")
 
# Print the resultant Dataframe
duplicate


# In[9]:


#Checking and dropping null values
df1.isnull().sum()


# In[12]:


# Drop Columns
df1.drop(columns ='RATE_INTEREST_PRIMARY', inplace = True)
df1.drop(columns ='RATE_INTEREST_PRIVILEGED', inplace = True)


# In[13]:


df2.isnull().sum()


# In[10]:


# checking for outliers
df1.describe()


# In[4]:


df2.describe()


# In[27]:


# Deleting Otliers From Code_gender
df2 = df2[df2.CODE_GENDER != 'XNA']


# In[29]:


type_count = df2.groupby('CODE_GENDER').CODE_GENDER.count()


# In[ ]:


# Visualization


# In[30]:


# Male and Female Count 
plt.figure(figsize=(4,4))
plt.title('Gender Distribution chart')
plt.pie(type_count,labels= type_count.index,autopct='%.1f',startangle=180)


# In[4]:


# Distribution of target
target_count = df2.groupby('TARGET').TARGET.count()


# In[12]:


plt.figure(figsize=(4,4))
plt.title('Target distribution')
plt.pie(target_count,labels= target_count.index,autopct='%.1f',startangle=180)


# In[99]:


df1 = df1[df1.NAME_CLIENT_TYPE != 'XNA']


# In[100]:


# distribution of client type
Client_type = df1.groupby('NAME_CLIENT_TYPE').NAME_CLIENT_TYPE.count()


# In[101]:


plt.figure(figsize=(4,4))
plt.title('Client Distribution chart')
plt.pie(Client_type,labels= Client_type.index,autopct='%.1f',startangle=180)


# In[119]:


# Income type distribution
Income_Type =df2['NAME_INCOME_TYPE'].value_counts().rename_axis('NAME_INCOME_TYPE').reset_index(name = 'counts')
sns.barplot(y='NAME_INCOME_TYPE', x ='counts', data= Income_Type).set(title='INCOME TYPE DISTRIBUTION')


# In[69]:


# Income type vs target
sns.set_style('whitegrid')
sns.set_context('talk',font_scale=0.7)

plt.figure(figsize=(5,5))
plt.rcParams["axes.labelsize"] = 15
plt.rcParams['axes.titlesize'] = 15
plt.rcParams['axes.titlepad'] = 15
plt.xticks(rotation=90)
plt.xscale('log')
plt.title('Distribution of Income Type with target')

ax = sns.countplot(data = df2, y= 'NAME_INCOME_TYPE', order=df2['NAME_INCOME_TYPE'].value_counts().index,
                   hue = 'TARGET',palette='bright')


# In[68]:


#occuoation type vs target
sns.set_style('whitegrid')
sns.set_context('talk', font_scale=0.7)

plt.figure(figsize=(5,5))
plt.rcParams["axes.labelsize"] = 15
plt.rcParams['axes.titlesize'] = 15
plt.rcParams['axes.titlepad'] = 15
plt.xticks(rotation=90)
plt.xscale('log')
plt.title('Distribution of Occupation Type with target')

ax = sns.countplot(data = df2, y= 'OCCUPATION_TYPE', order=df2['OCCUPATION_TYPE'].value_counts().index,
                   hue = 'TARGET',palette='bright')


# In[71]:


# Education vs Type
sns.set_style('whitegrid')
sns.set_context('talk', font_scale=0.7)

plt.figure(figsize=(5,5))
plt.rcParams["axes.labelsize"] = 15
plt.rcParams['axes.titlesize'] = 15
plt.rcParams['axes.titlepad'] = 15
plt.xticks(rotation=90)
plt.xscale('log')
plt.title('Distribution of Education Type with target')

ax = sns.countplot(data = df2, y= 'NAME_EDUCATION_TYPE', order=df2['NAME_EDUCATION_TYPE'].value_counts().index,
                   hue = 'TARGET',palette='bright')


# In[118]:


# Heat map
plt.figure(figsize=(20, 8))
plt.rcParams["axes.labelsize"] = 10
dataplot = sns.heatmap(df1.corr(), cmap="YlGnBu", annot=True)
  
# displaying heatmap
plt.show()

