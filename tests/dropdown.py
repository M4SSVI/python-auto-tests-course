import math
import allure
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects2.html"
driver = webdriver.Chrome()
driver.get(link)

x_element = driver.find_element_by_id("num1")
x = x_element.text


y_element = driver.find_element_by_id("num2")
y = y_element.text

value = int(x) + int(y)

select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(str(value))

# Отправляем заполненную форму
button = driver.find_element_by_css_selector("button.btn")
button.click()
