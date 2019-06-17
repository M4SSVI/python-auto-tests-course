import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 10).until(
EC.text_to_be_present_in_element((By.ID, "price"), "10000")
 )

button = browser.find_element_by_css_selector("[id=book]")
button.click()

x_element = browser.find_element_by_css_selector("[id=input_value]")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_css_selector("[id=answer]")
input1.send_keys(y)

button = browser.find_element_by_css_selector("[id=solve]")
button.click()
