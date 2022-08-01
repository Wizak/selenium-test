from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import json


url = 'https://diia.gov.ua/'

driver = webdriver.Chrome('./chromedriver')
driver.get(url)

chatbot_button = driver.find_element(By.ID, 'chatbot_btn')
chatbot_button.click()

time.sleep(1)

chatbot_list = driver.find_element(By.CLASS_NAME, 'chatbot_list')

chatbot_dict = {}
for chatbot in chatbot_list.find_elements(By.CLASS_NAME, 'chatbot_item'):
    chatbot_name = chatbot.text
    chatbot_href = chatbot.get_attribute('href')
    chatbot_dict[chatbot_name] = chatbot_href

with open('chatbot_list.json', 'w') as f:
    json.dump(chatbot_dict, f, indent=3)

time.sleep(1)
driver.close()
