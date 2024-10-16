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

login_standard_user = "standard_user"
password_all = "secret_sauc"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input login')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input password')
login_button = driver.find_element(by=By.ID, value="login-button")
login_button.click()
print('Click login button')
# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# print(text_products.text)
# # assert value_text_products == 'Products'
# # print('True')

# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('True')

warning_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_message = warning_message.text
assert value_warning_message == "Epic sadface: Username and password do not match any user in this service"
print('True')