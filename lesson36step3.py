import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_green_people(browser, links):
    link = f"{links}/"
    answer = math.log(int(time.time()))
    browser.get(link)
    browser.implicitly_wait(60)
    input = browser.find_element_by_css_selector("textarea.textarea.ember-text-area.ember-view")
    input.send_keys(f"{answer}")
    submit = browser.find_element_by_css_selector("button.submit-submission")
    submit.click()
    check = browser.find_element_by_css_selector("pre.smart-hints__hint")
    correct_msg = check.text
    assert correct_msg == "Correct!", f"Ответ отличается: {check}"