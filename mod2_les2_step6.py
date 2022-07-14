from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)


input1 = browser.find_element(By.ID, 'input_value')
x = input1.text

ans = str(log(abs(12*sin(int(x)))))

input2 = browser.find_element(By.ID, "answer")
input2.send_keys(ans)

button1 = browser.find_element(By.CSS_SELECTOR, "[type = 'Checkbox']")
button1.click()

button2 = browser.find_element(By.CSS_SELECTOR, "[value = 'robots']")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
button2.click()

button3 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
button3.click()

time.sleep(10)
browser.quit()
