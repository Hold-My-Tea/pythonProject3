
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


######Login user
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



all_products = {'1' : 'Sauce Labs Backpack', '2' : 'Sauce Labs Bike Light', '3' : 'Sauce Labs Bolt T-Shirt',
              '4' : 'Sauce Labs Fleece Jacket', '5' : 'Sauce Labs Onesie', '6' :'Test.allTheThings() T-Shirt (Red)'}

#### Choose product
print('Приветствуем тебя в нашем интернет магазине')
print(f'Выбери один из следующих товароd и укажи его номер: {all_products}')
product = input()
print(product)
product_name = all_products[product]
print(product_name)


####Info my product
my_product = driver.find_element(By.XPATH, "//div[contains(text(), '" + all_products[product] +"')]")
value_my_product = my_product.text
print(value_my_product)

price_my_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[" + product + "]/div[2]/div["
                                                                                                   "2]/div")
value_price_my_product = price_my_product.text
print(value_price_my_product)

### Add my product to cart
product_edited = all_products[product].lower()
l = product_edited.split()
product_edited_2 = '-'.join(l)
print(product_edited_2)


add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-" + product_edited_2 + "']")
add_to_cart_button.click()
print('Click add_to_cart button')


cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print('Click cart button')

###Info in cart
cart_my_product = driver.find_element(By.XPATH, "//div[contains(text(), '" + all_products[product] +"')]")
cart_value_my_product = cart_my_product.text
print(cart_value_my_product)
assert value_my_product == cart_value_my_product
print('My product is correct')

cart_price_my_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
cart_value_price_my_product = cart_price_my_product.text
print(cart_value_price_my_product)
assert value_price_my_product == cart_value_price_my_product
print('Price of my product is correct')


checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print('Click checkout button')

#### Info User
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

###Info finish
finish_my_product = driver.find_element(By.XPATH, "//div[contains(text(), '" + all_products[product] +"')]")
finish_value_my_product = finish_my_product.text
print(finish_value_my_product)
assert value_my_product == finish_value_my_product
print('My product is correct')

finish_price_my_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
finish_value_price_my_product = finish_price_my_product.text
print(finish_value_price_my_product)
assert value_price_my_product == finish_value_price_my_product
print('Price of my product is correct')

###Total price
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
assert value_summary_price == "Item total: " + value_price_my_product
print('Total price is correct')