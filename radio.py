import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

from selenium import webdriver
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_css_selector("[id=answer]")
input1.send_keys(y)
# Указать чекбокс
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()
# Выбрать радиотбаттон
option2 = browser.find_element_by_css_selector("[for='robotsRule']")
option2.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
