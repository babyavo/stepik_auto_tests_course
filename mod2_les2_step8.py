from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
    input1.send_keys("F")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
    input2.send_keys("U")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
    input3.send_keys("CK")

    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'genome.txt')

    l_path = "C:/Users/user/Desktop/lol.txt"

    element = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
    element.send_keys(l_path)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
