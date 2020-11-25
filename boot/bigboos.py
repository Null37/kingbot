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
#chromrdriver = "C:\Program Files (x86)\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromrdriver
#driver = webdriver.Chrome(chromrdriver)
#driver.maximize_window()
number_page = '1'
url = 'https://www.redbubble.com/shop/?' + 'page=' + number_page + '&query=' + serch
href = []
def get_click_href(url):
	i = 0
	r = requests.get(url) 
	soup = BeautifulSoup(r.text, 'lxml')
	site = soup.find_all('a', {'class' : 'styles__link--2sYi3'})
	for s in site:
		href.append(s['href'])
	print(href[0])
get_click_href(url)