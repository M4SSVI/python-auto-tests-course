import allure
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
link = "https://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()
driver.get(link)
driver.execute_script("window.scrollBy(0, 100);")

x_element = driver.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

input1 = driver.find_element_by_css_selector("[id=answer]")
input1.send_keys(y)
# Указать чекбокс
option1 = driver.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()
# Выбрать радиотбаттон
option3 = driver.find_element_by_css_selector("[id=robotsRule]")
option3.click()

#Найти кнопку 
button = driver.find_element_by_tag_name("button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
