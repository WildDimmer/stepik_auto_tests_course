import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath('C:\\Users\\User\Desktop\\Степик_Селениум')
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("*")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("**")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("***")
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()
    time.sleep(10)
finally:
    time.sleep(10)
    browser.quit()

