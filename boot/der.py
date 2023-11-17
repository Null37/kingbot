import os.path
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

serch = "poster attack on titan"
sleep = 4
chromrdriver = "C:\Program Files (x86)\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)

url2 = 'https://www.redbubble.com/shop/?' + 'page=' + a + '&query=' + serch


def next_page(url2):
    driver.get(url2)
    driver.maximize_window()
    for _ in range(15):
        time.sleep(sleep)
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        soup = BeautifulSoup(r.txt, 'lxml')


next_page(url2)
