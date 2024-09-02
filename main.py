import time
import os
from datetime import datetime, time as dt_time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

print(time.ctime())
site_url = os.environ.get("URL2")
load_dotenv()
field1 = os.environ.get('FIELD1')
field2 = os.environ.get('FIELD2')
field3 = os.environ.get('FIELD3')
field4 = os.environ.get('FIELD4')
field5 = os.environ.get('FIELD5')

chrome_browser = webdriver.Chrome()

script_done = False
while not script_done:
    chrome_browser.get(site_url)
    document_type = chrome_browser.find_element(By.ID, field1)
    document_type.click()
    document_type.send_keys(Keys.ARROW_DOWN)
    document_type.send_keys(Keys.ENTER)
    time.sleep(3)
    document_number = chrome_browser.find_element(By.ID, field2)
    document_number.send_keys("112345")
    time.sleep(3)
    document_issue_place = chrome_browser.find_element(By.ID, field3)
    document_issue_place.send_keys("Bogota")
    time.sleep(3)
    document_issue_date = chrome_browser.find_element(By.ID, field4)
    document_issue_date.click()
    document_issue_date.send_keys("02045677")
    time.sleep(3)
    birth_date = chrome_browser.find_element(By.ID, field5)
    birth_date.click()
    birth_date.send_keys("01012000")
    time.sleep(3)
    script_done = True

input("Press ENTER to close the browser....")
