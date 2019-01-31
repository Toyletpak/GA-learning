#!/usr/bin/env python
# coding: utf-8

# # Approach
# 
# - Use selenium to scrape all href links for results to 'data' search on site of choice
# - Compile a list of links
# - Iterate through each link to grab the relevant information field
# - Key info: Job Title, Location, Company, Salary Range, Salary format, Position Seniority, Employment Type, Requirements

# In[1]:


# Import the world!
import os
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import pandas as pd


# In[4]:


# Opening the driver
driver = webdriver.Chrome('/Users/paklun/Desktop/materials-master/projects/project-4/chromedriver')


# ## First Pass to retrieve links and region

# In[3]:


linkslist = []
regionlist = []

for x in range(0,210):
    URL = "https://www.mycareersfuture.sg/search?search=Data&sortBy=new_posting_date&page=%d" % x
    driver.get(URL)
    sleep(random.randint(5,8))
    
    for i in range(0,20):
        jobcard_xpath_iter = '//*[@id="job-card-%d"]/div/a' % i
        jobcards = driver.find_elements_by_xpath(jobcard_xpath_iter)
        
        for jobs in jobcards:
            joblink = jobs.get_attribute('href')
            linkslist.append(joblink)
            
    for j in range(0,20):
        region_xpath_iter = '//*[@id="job-card-%d"]/div/a/div[1]/div[1]/section/div[2]/div[2]/section/p[1]' % j
        regions = driver.find_elements_by_xpath(region_xpath_iter)
        
        for locale in regions:
            region = locale.text
            regionlist.append(region)

    print('Getting page ... %d' %x ,'..fetching..',len(linkslist),'of',len(regionlist) )


# In[ ]:


# Saving to a dataframe

linktable = pd.DataFrame({'Links':linkslist,'Region':regionlist})


# In[ ]:


# Saving to a csv file

linktable.to_csv('Career_Links_new.csv')


# ## Reading into the links to scrape more info

# In[ ]:


# IN THE NEXT FILE


# In[ ]:


# Closes the driver
driver.close()

