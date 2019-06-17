import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

from selenium import webdriver
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome('/Users/user/bin/chromedriver')
browser.get(link)

x_element = browser.find_element_by_css_selector("[id=treasure]")
treasure = x_element.get_attribute("valuex")
x = calc(treasure)

input1 = browser.find_element_by_css_selector("[id=answer]")
input1.send_keys(x)
# Указать чекбокс
option2 = browser.find_element_by_css_selector("[id=robotCheckbox]")
option2.click()
# Выбрать радиотбаттон
option3 = browser.find_element_by_css_selector("[id=robotsRule]")
option3.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
