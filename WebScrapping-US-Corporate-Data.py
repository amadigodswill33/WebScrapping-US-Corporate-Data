#!/usr/bin/env python
# coding: utf-8

# # Website Scraping Project

# In[2]:


import requests


# In[11]:


from bs4 import BeautifulSoup
url= 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[12]:


print(soup)


# In[13]:


soup.find_all('table')[1]


# In[14]:


table =soup.find_all('table')[1]


# In[15]:


soup.find_all('table', class_ = 'wikitable sortable')


# In[16]:


world_title= table.find_all('th')


# In[17]:


print(world_title)


# In[18]:


world_table_title = [title.text.strip() for title in world_title]


# In[19]:


print(world_table_title)


# In[20]:


import pandas as pd


# In[21]:


df=pd.DataFrame(columns = world_table_title)


# In[22]:


print(df)


# In[23]:


column_data= table.find_all('tr')


# In[24]:


print(column_data)


# In[25]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)


# In[26]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[27]:


print(df)


# In[28]:


df.to_csv(r'C:\Users\User\Desktop\My_DataSet\ScrapedProject_comapanies.csv', index = False)

