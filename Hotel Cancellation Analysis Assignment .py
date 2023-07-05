#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress


# In[2]:


#bring in our data
df1= pd.read_excel(r'C:\Users\gonza\OneDrive\Desktop\Python for Power Bi Course\hotel_revenue_historical_full.xlsx',sheet_name = "2018")
df2= pd.read_excel(r'C:\Users\gonza\OneDrive\Desktop\Python for Power Bi Course\hotel_revenue_historical_full.xlsx',sheet_name = "2019")
df3= pd.read_excel(r'C:\Users\gonza\OneDrive\Desktop\Python for Power Bi Course\hotel_revenue_historical_full.xlsx',sheet_name = "2020")
full_dataset = pd.concat([df1, df2, df3], ignore_index=True)
full_dataset.tail(5)


# In[3]:


full_dataset['is_canceled'].value_counts()


# In[4]:


#wrap this into the dataset to show the filtered the dataset excluding cancelations 
full_dataset['is_canceled']!=1


# In[5]:


filtered_data = full_dataset[full_dataset['is_canceled']!=1]
filtered_data.info()


# In[6]:


#univariate and bivariate analysis
sns.distplot(filtered_data['adr'])


# In[7]:


sns.distplot(filtered_data['lead_time'])


# In[8]:


plt.figure(figsize=(8,5))
sns.boxplot(y=filtered_data['lead_time'],showfliers=False)     #copied a piece of this line and input into the
                                                               #..dict{xx} and specified ".2f" decimals
plt.title(f"The Mean is {filtered_data['lead_time'].mean():.2f}")


# In[9]:


plt.figure(figsize=(8,5))
sns.violinplot(data= filtered_data, y='lead_time',x= 'hotel') 
resort_mean =  filtered_data[filtered_data['hotel'] == 'Resort Hotel']['lead_time'].mean()
city_mean = filtered_data[filtered_data['hotel'] == 'City Hotel']['lead_time'].mean()
plt.title(f"The Mean is {filtered_data['lead_time'].mean():.2f} and Resort Mean is {resort_mean:.2f} and the City Mean is {city_mean:.2f}") 


# In[10]:


sns.distplot(filtered_data[filtered_data['hotel'] == 'City Hotel']['adr'], label='City Hotel')
sns.distplot(filtered_data[filtered_data['hotel'] == 'Resort Hotel']['adr'], label= 'Resort Hotel')

resort_mean =  filtered_data[filtered_data['hotel'] == 'Resort Hotel']['adr'].mean()
city_mean = filtered_data[filtered_data['hotel'] == 'City Hotel']['adr'].mean()

plt.axvline(resort_mean, color='black', linestyle="--", label='Resort Mean')
plt.axvline(city_mean, color='red', linestyle="--", label='City Mean')


plt.title(f"The Mean is {filtered_data['adr'].mean():.2f} and Resort Mean is {resort_mean:.2f} and the City Mean is {city_mean:.2f}") 
plt.legend()


# In[11]:


#bivariate analysis and linear regression 


# In[ ]:




