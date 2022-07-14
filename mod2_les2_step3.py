from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "num1")
    x = input1.text
    input2 = browser.find_element(By.ID, "num2")
    y = input2.text

    sum = int(x) + int(y)

    button1 = browser.find_element(By.TAG_NAME, "select")
    button1.click()

    button2 = browser.find_element(By.CSS_SELECTOR, f"[value = '{sum}']")
    button2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()