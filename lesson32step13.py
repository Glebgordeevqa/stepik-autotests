from selenium import webdriver
import unittest

class TestAbs(unittest.TestCase):
    def test_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(3)
        input1 = browser.find_element_by_css_selector(".first_block>.first_class>input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block>.second_class>input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block>.third_class>input.third")
        input3.send_keys("Smolensk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "noice")
        browser.quit()

    def test_second(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(3)
        input1 = browser.find_element_by_css_selector(".first_block>.first_class>input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block>.second_class>input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block>.third_class>input.third")
        input3.send_keys("Smolensk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "noice")
        browser.quit()

if __name__ == '__main__':
    unittest.main()
