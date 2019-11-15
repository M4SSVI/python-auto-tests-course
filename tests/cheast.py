import math
import allure

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()
driver.get(link)

x_element = driver.find_element_by_css_selector("[id=treasure]")
treasure = x_element.get_attribute("valuex")
x = calc(treasure)

input1 = driver.find_element_by_css_selector("[id=answer]")
input1.send_keys(x)
# Указать чекбокс
option2 = driver.find_element_by_css_selector("[id=robotCheckbox]")
option2.click()
# Выбрать радиотбаттон
option3 = driver.find_element_by_css_selector("[id=robotsRule]")
option3.click()

# Отправляем заполненную форму
button = driver.find_element_by_css_selector("button.btn")
button.click()
