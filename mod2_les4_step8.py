from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    y = calc(x)

    input2 = browser.find_element(By.CLASS_NAME, "form-control")
    input2.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()