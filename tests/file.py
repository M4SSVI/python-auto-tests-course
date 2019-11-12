import os 
import allure
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля

# Заполняем поле имя
input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
input1.send_keys("Ivan")
# Заполняем поле фамилия
input2 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
input2.send_keys("Petrov")
# Заполняем поле email
input3 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
input3.send_keys("test@mail.com")

input4 = browser.find_element_by_id("file")
input4.click()

current_dir = os.path.abspath(os.path.dirname(__/user/files__))     # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
