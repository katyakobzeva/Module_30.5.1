import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Firefox('')
   pytest.driver.maximize_window()
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, 'email')))
   # Ввод эл. адреса
   pytest.driver.find_element(By.ID, 'email').send_keys('test02test@bk.ru')

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, 'pass')))
   # Ввод пароля
   pytest.driver.find_element(By.ID, 'pass').send_keys('123456789')

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Клик по кнопе "Войти"
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
   # Клик по ссылке "Мои питомцы"
   pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()


   #установка неявного ожидания
   pytest.driver.implicitly_wait(10)

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
