import allure
import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
link = "http://suninjuly.github.io/registration2.html"
driver.get(link)

# Ваш код, который заполняет обязательные поля

# Заполняем поле имя
input1 = driver.find_element_by_css_selector("[placeholder='Input youjrtgkjrtiojlktrjbjkrtr name']")
input1.send_keys("Ivan")
# Заполняем поле фамилия
input2 = driver.find_element_by_css_selector("[placeholder='Input your email']")
input2.send_keys("Petrov")
# Заполняем поле email
input3 = driver.find_element_by_css_selector("[placeholder='Input your phone']")
input3.send_keys("test@mail.com")
# Заполняем поле адрес
input4 = driver.find_element_by_css_selector("[placeholder='Input your address']")
input4.send_keys("test@mail.com")

# Отправляем заполненную форму
button = driver.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = driver.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text
