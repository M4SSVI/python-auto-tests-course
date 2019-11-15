import allure
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)


driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.ID, "price"), "10000")
 )

button = driver.find_element_by_css_selector("[id=book]")
button.click()

x_element = driver.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

input1 = driver.find_element_by_css_selector("[id=answer]")
input1.send_keys(y)

button = driver.find_element_by_css_selector("[id=solve]")
button.click()
