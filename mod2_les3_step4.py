from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    y = calc(x)

    input2 = browser.find_element(By.CLASS_NAME, "form-control")
    input2.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()