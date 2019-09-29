from selenium import webdriver
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    input1 = browser.find_element_by_css_selector("div.form-group>input#answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("div.form-check>#robotCheckbox")
    option1.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option2 = browser.find_element_by_css_selector("div.form-radio-custom>input.form-check-input")
    option2.click()
    submit = browser.find_element_by_css_selector("button.btn-primary")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()