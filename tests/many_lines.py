import allure
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/huge_form.html")

elements = driver.find_elements_by_tag_name("input")
for element in elements:
    element.send_keys("Мой ответ")

button = driver.find_element_by_css_selector("button.btn")
button.click()
