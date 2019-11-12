import allure
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

from selenium import webdriver
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

first_window = browser.window_handles[0]

button = browser.find_element_by_css_selector("button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


x_element = browser.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_css_selector("[id=answer]")
input1.send_keys(y)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
