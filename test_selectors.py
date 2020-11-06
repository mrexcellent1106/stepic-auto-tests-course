from selenium import webdriver
import time
import unittest

class TestSelectors(unittest.TestCase):

    def testReg1(self):
        assert_message = "Congratulations! You have successfully registered!"
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        element = browser.find_element_by_css_selector('input:required.first')
        element.send_keys('test')
        element2 = browser.find_element_by_css_selector('input:required.second')
        element2.send_keys('test')
        element3 = browser.find_element_by_css_selector('input:required.third')
        element3.send_keys('test')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, assert_message, f"Should be ''{assert_message}'', but it's ''{welcome_text}''" )

    def testReg2(self):
        assert_message = "Congratulations! You have successfully registered!"
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        element = browser.find_element_by_css_selector('input:required.first')
        element.send_keys('test')
        element2 = browser.find_element_by_css_selector('input:required.second')
        element2.send_keys('test')
        element3 = browser.find_element_by_css_selector('input:required.third')
        element3.send_keys('test')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, assert_message, f"Should be '{assert_message}', but it's '{welcome_text}'")

if __name__ == "__main__":
    unittest.main()
