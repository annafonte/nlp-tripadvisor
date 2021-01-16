#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Importing libraries
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait       
import sys
import csv
import time

# default path to file to store data
path_to_file = "/Users/annafonte/Documents/Ironhack/Final_project/reviews_test.csv"
path = "/Users/annafonte/Documents/Ironhack/Final_project/chromedriver"

# number of scraped pages (change it later to scrape more)
num_page = 5000

# default tripadvisor website of hotel or attraction
url = "https://www.tripadvisor.com/Attraction_Review-g187497-d190166-Reviews-Basilica_of_the_Sagrada_Familia-Barcelona_Catalonia.html"

# if you pass the inputs in the command line
if (len(sys.argv) == 4):
    path_to_file = sys.argv[1]
    num_page = int(sys.argv[2])
    url = sys.argv[3]

# import the webdriver
driver = webdriver.Chrome(path)
driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'a')
csvWriter = csv.writer(csvFile)

# iterating through the different pages
for i in range(0, num_page):
    try: 
        # expand the review 
        time.sleep(3)
        expand = driver.find_element_by_xpath(".//div[contains(@data-test-target, 'expand-review')]")
        driver.execute_script("arguments[0].click();", expand)
        # Creating variable with the container of the reviews
        container = driver.find_elements_by_xpath("//div[@data-reviewid]")
        countries = driver.find_elements_by_xpath(".//span[@class='default _3J15flPT small']")
        
    except:
        pass
    
    # Iterating through the review container to get rating, title, review and date + Write info in csv
    for j in range(len(container)):
        try:
            rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
            title = container[j].find_element_by_xpath(".//div[contains(@data-test-target, 'review-title')]").text
            review = container[j].find_element_by_xpath(".//q[@class='IRsGHoPm']").text.replace("\n", "  ")
            date = container[j].find_element_by_xpath(".//span[@class='_34Xs-BQm']").text
            country = " ".join(countries[j].text.split(" "))
        except:
            pass 
            
            csvWriter.writerow([date, country, rating, title, review]) 
    
    try:    
    # changing to next page 
        time.sleep(6)
        button = driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]')
        driver.execute_script("arguments[0].click();", button)
    except:
        pass

     
driver.quit()


# In[ ]:




