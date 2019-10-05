from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    value_x = x_element.get_attribute("valuex")
    x = value_x
    y = calc(x)
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("input.check-input#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("input.check-input#robotsRule")
    option2.click()
    time.sleep(1)
    submit = browser.find_element_by_css_selector("button.btn-default")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()