from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin, log


# Задание: принимаем alert
try:
    # Запуск браузера и открытие веб-страницы
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск и нажатие кнопки
    button = browser.find_element(By.XPATH, "//*[@type='submit']")
    button.click()

    # Переключение на модальное окно и принять его
    confirm = browser.switch_to.alert
    confirm.accept()

    # Функция для подсчёта формулы
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    # Поиск элемента по локатору, считывние текста (число) элемента, расчет y с помощью функции
    element1 = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = element1.text
    y = calc(x)

    # Поиск элемента по локатору, отправка результатов расчёта формулы в поле ввода
    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)

    # Поиск и нажатие кнопки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # Выгрузка страницы браузера из памяти компьтера
    browser.quit()
