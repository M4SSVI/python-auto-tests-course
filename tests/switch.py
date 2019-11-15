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
link = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
driver.get(link)

first_window = driver.window_handles[0]

button = driver.find_element_by_css_selector("button.btn")
button.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)


x_element = driver.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

input1 = driver.find_element_by_css_selector("[id=answer]")
input1.send_keys(y)

# Отправляем заполненную форму
button = driver.find_element_by_css_selector("button.btn")
button.click()
