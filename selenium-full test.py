import time
from argparse import Action

from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input login')
# time.sleep(3)
# user_name.clear()

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input password')
login_button = driver.find_element(by=By.ID, value="login-button")
login_button.click()
print('Click login button')

"""Info product 1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart_button.click()
print('Click add_to_cart button')

cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print('Click cart button')

""""Info cart product 1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
cart_value_product_1 = cart_product_1.text
print(cart_value_product_1)
assert value_product_1 == cart_value_product_1
print('True')

cart_price_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
cart_value_price_product_1 = cart_price_product_1.text
print(cart_value_price_product_1)
assert value_price_product_1 == cart_value_price_product_1
print('True')

checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print('Click checkout button')

""""Info User"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Oksana')
print('Input first name')

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Mayer')
print('Input last name')

zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_code.send_keys('12345')
print('Input zip_code')

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print('Click continue button')

""""Info finish"""
finish_cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
finish_cart_value_product_1 = finish_cart_product_1.text
print(finish_cart_value_product_1)
assert value_product_1 == finish_cart_value_product_1
print('True')

finish_cart_price_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
finish_cart_value_price_product_1 = finish_cart_price_product_1.text
print(finish_cart_value_price_product_1)
assert value_price_product_1 == finish_cart_value_price_product_1
print('True')

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = 'Item total: ' + finish_cart_value_price_product_1
assert value_summary_price == item_total
print('True')


# menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
# menu.click()
# print('Click menu button')
# time.sleep(3)
#
# link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
# link_about.click()
# print('Click link button')
# url = 'https://saucelabs.com/'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('True')