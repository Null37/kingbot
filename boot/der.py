import requests
import urllib3
from bs4 import BeautifulSoup
import os
import os.path
import base64 
from selenium import webdriver
from os.path  import basename
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

serch = "poster attack on titan"
sleep = 4
chromrdriver = "C:\Program Files (x86)\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)

url2 = 'https://www.redbubble.com/shop/?' + 'page=' + a + '&query=' + serch
def next_page(url2):
	driver.get(url2)
	driver.maximize_window()
	i = 0
	while i < 15:
		time.sleep(sleep)
		driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
		i += 1
		soup = BeautifulSoup(r.txt, 'lxml')
next_page(url2)