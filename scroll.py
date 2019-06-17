import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

from selenium import webdriver
link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
browser.execute_script("window.scrollBy(0, 100);")

x_element = browser.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_css_selector("[id=answer]")
input1.send_keys(y)
# Указать чекбокс
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()
# Выбрать радиотбаттон
option3 = browser.find_element_by_css_selector("[id=robotsRule]")
option3.click()

#Найти кнопку 
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
