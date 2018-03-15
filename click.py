from selenium import webdriver
import os
import time


x = os.getcwd()

browser = webdriver.Chrome()
browser.get(x+r"/presentation.html")


for x in range(0,5):
    ele = browser.find_element_by_id("next")
    time.sleep(5)
    ele.click()
