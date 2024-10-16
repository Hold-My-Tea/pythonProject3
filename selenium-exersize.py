
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

"""Login user"""
login_standard_user = "standard_user"
password_all = "secret_sauce"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input login')
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

"""Info product 2"""
product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
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
print('Product 1 is correct')

cart_price_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
cart_value_price_product_1 = cart_price_product_1.text
print(cart_value_price_product_1)
assert value_price_product_1 == cart_value_price_product_1
print('Price of product 1 is correct')

""""Info cart product 2"""
cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
cart_value_product_2 = cart_product_2.text
print(cart_value_product_2)
assert value_product_2 == cart_value_product_2
print('Product 2 is correct')

cart_price_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
cart_value_price_product_2 = cart_price_product_2.text
print(cart_value_price_product_2)
assert value_price_product_2 == cart_value_price_product_2
print('Price of product 2 is correct')

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
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
finish_value_product_1 = finish_product_1.text
print(finish_value_product_1)
assert value_product_1 == finish_value_product_1
print('Product 1 is correct')

finish_price_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
finish_value_price_product_1 = finish_price_product_1.text
print(finish_value_price_product_1)
assert value_price_product_1 == finish_value_price_product_1
print('Price of product 1 is correct')


finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
finish_value_product_2 = finish_product_2.text
print(finish_value_product_2)
assert value_product_2 == finish_value_product_2
print('Product 2 is correct')

finish_price_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
finish_value_price_product_2 = finish_price_product_2.text
print(finish_value_price_product_2)
assert value_price_product_2 == finish_value_price_product_2
print('Price of product 2 is correct')

""""Total price"""

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
total = (float(finish_value_price_product_1[1:]) + float(finish_value_price_product_2[1:]))
item_total = 'Item total: $' + str(total)
assert value_summary_price == item_total
print('Total price is correct')