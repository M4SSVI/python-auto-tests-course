import allure
import pytest


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def test_exception1():
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            driver.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        driver.quit()

def test_exception2():
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            driver.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        driver.quit()