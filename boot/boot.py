import os
import os.path
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

serch = "poster attack on titan"
sleep = 4
chromrdriver = "C:\Program Files (x86)\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.maximize_window()
url = f'https://www.redbubble.com/shop/?query={serch}'
driver.get(url)
driver.maximize_window()


def scrol_loop():
    for _ in range(15):
        time.sleep(sleep)
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)


def next_page(url2):
    driver.get(url2)
    driver.maximize_window()
    scrol_loop(driver)
    2


def scrol_and_download(url, number_of_the_page):
    scrol_loop()
    num = str(number_of_the_page)
    file_name = serch + num + ".html"
    file_exists = os.path.isfile(file_name)
    html = driver.page_source
    path = os.getcwd()
    if not os.path.exists(serch + num):
        os.makedirs(serch + num)
    if file_exists:
        with open(file_name, 'w', newline='', encoding="utf-8") as file:
            file.write(html)
    else:
        with open(file_name, 'x', newline='', encoding="utf-8") as file:
            file = open(file_name, 'w', newline='', encoding="utf-8")
            file.write(html)
    file.close()

    driver.close()
    with open(file_name, newline='', encoding="utf-8") as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'lxml')
        images = soup.find_all('img', {
            'class': 'styles__image--2CwxX styles__productImage--3ZNPD styles__rounded--1lyoH styles__fluid--3dxe-'})
    path = serch
    for image in images:
        name = image['alt']
        link = image.get('src')
        with open(os.path.join(path,
                               name.replace(' ', '-').replace('/', '').replace('|', '').replace('?', '-').replace('*',
                                                                                                                  '--0--')) + '.jpg',
                  'wb') as f:
            f.write(requests.get(link).content)


scrol_and_download(url)

# url2 = 'https://www.redbubble.com/shop/?' + 'page=2' + 'query=' + serch
