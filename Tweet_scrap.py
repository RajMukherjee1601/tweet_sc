#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium.webdriver.common.by import By



headers = {
    'authority': 'scrapeme.live',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}  # this is use to tell zomato website from which source or which user is accessing their website because zomato use secure network

driver = webdriver.Chrome()  # this is selenium driver which is use to automate the website
driver.get(input("Enter the link"))  # zomato URL for getting data
time.sleep(2)  # time dealy for wait to open website
scroll_pause_time = 3  # scroll time  by which zomato website auto scroll after each 3 second
screen_height = driver.execute_script("return window.screen.height;")  # this is use to define screen height
i = 1

while True:  # run a loop until website reach end of the page

    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height,
                                                                            i=i))  # its execute scroll positions
    i += 1
    time.sleep(scroll_pause_time)

    scroll_height = driver.execute_script("return document.body.scrollHeight;")

    if (screen_height) * i > scroll_height:
        break  # when website reach end of the page then while loop break

soup = BeautifulSoup(driver.page_source, "html.parser")  # this is use to get the data from the page open above
print(soup.get_text())

