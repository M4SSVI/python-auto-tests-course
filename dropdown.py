import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text


y_element = browser.find_element_by_id("num2")
y = y_element.text

value = int(x) + int(y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(value))

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
