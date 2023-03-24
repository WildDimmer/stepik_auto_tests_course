import time
import os
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
link = "http://suninjuly.github.io/explicit_wait2.html" 
browser = webdriver.Chrome()
browser.get(link)
ready = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
if ready:
    button = browser.find_element(By.CSS_SELECTOR, "[id='book']").click()
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = int(x_element.text)
    sin = math.sin(x)
    abs = math.fabs(12*sin)
    decision = math.log(abs)
    deci = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    deci.send_keys(decision)
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button2.click()
    time.sleep(5)


 