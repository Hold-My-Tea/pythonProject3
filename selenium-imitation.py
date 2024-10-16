import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Keys

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

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input password')

password.send_keys(Keys.RETURN)

filter_1 = driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']")
filter_1.click()
print('Click filter')
time.sleep(3)
filter_1.send_keys(Keys.DOWN)
time.sleep(3)
filter_1.send_keys(Keys.RETURN)

current_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot.png' + current_date + '.png'
driver.save_screenshot('C:\\Users\\Oksana\\AQA\\pythonProject3\\screen\\' + name_screenshot)

# time.sleep(3)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(3)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(3)
# user_name.send_keys('er')


# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print('Input password')
# login_button = driver.find_element(by=By.ID, value="login-button")
# login_button.click()
# print('Click login button')
# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# print(text_products.text)
# assert value_text_products == 'Products'
# print('True')

# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('True')
