#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the world!
import os
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import pandas as pd
import numpy as np


# ## Part Two : Entering links to pick data

# In[3]:


csv = './Career_Links_new.csv'
df = pd.read_csv(csv)


# In[6]:


df.head()


# In[60]:


# Opening the driver
driver = webdriver.Chrome('/Users/paklun/Desktop/materials-master/projects/project-4/chromedriver')

# Setting up lists
company=[]
title=[]
employment=[]
seniority=[]
industry=[]
salary=[]
payment=[]
description=[]
requirements=[]
count=0

# Looping through links to scrape data, impute Nan if error

for x in df.Links:
    driver.get(x)
    count +=1
    sleep(random.randint(5,8))
    print('Currently Scraping Link No.',count)
    
    try:
        company.append(driver.find_element_by_name('company').text)
    except:
        company.append(np.nan)
    try:
        title.append(driver.find_element_by_id('job_title').text)
    except:
        title.append(np.nan)    
    try:
        employment.append(driver.find_element_by_id('employment_type').text)
    except:
        employment.append(np.nan)
    try:
        seniority.append(driver.find_element_by_id('seniority').text)
    except:
        seniority.append(np.nan)
    try:
        industry.append(driver.find_element_by_id('job-categories').text)
    except:
        industry.append(np.nan)
    try:
        salary.append(driver.find_element_by_class_name('lh-solid').text)
    except:
        salary.append(np.nan)
    try:
        payment.append(driver.find_element_by_class_name('salary_type').text)
    except:
        payment.append(np.nan)      
    try:
        description.append(driver.find_element_by_id('job_description').text)
    except:
        description.append(np.nan)
    try:
        requirements.append(driver.find_element_by_id('requirements').text)
    except:
        requirements.append(np.nan)
    


# In[61]:


data = pd.DataFrame({'Company':company,'Title':title,'Employment Type':employment,'Seniority':seniority,'Industry':industry,'Salary':salary,'Payment':payment,'Description':description, 'Requirements':requirements })


# In[62]:


data


# In[65]:


result = pd.concat([df,data], axis=1,sort=False)


# In[66]:


result.to_csv('Career_Database.csv')


# In[67]:


# Closes the driver
driver.close()


# In[ ]:




