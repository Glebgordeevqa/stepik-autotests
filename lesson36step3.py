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

@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_green_people(browser, links):
    link = f"{links}/"
    answer = math.log(int(time.time()))
    browser.get(f"https://stepik.org/lesson/{links}/step/1")
    browser.implicitly_wait(60)
    browser.find_element_by_css_selector("textarea.textarea.ember-text-area.ember-view").send_keys(f"{answer}")
    browser.find_element_by_css_selector("button.submit-submission").click()
    check = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    assert check == "Correct!", f"Ответ отличается: {check}"