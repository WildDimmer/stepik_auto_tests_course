from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math  
try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()    
    browser.get(link) 
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = int(x_element.text)
    sin = math.sin(x)
    abs = math.fabs(12*sin)
    decision = math.log(abs)
    # decision = str(math.log(abs(12*math.sin(int(x)))))
    deci = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", deci)    
    deci.send_keys(decision)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    time.sleep(10)
finally:
    time.sleep(10)
    browser.quit()

