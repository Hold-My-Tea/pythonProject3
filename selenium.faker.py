from faker import Faker
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

faker = Faker("en_US")
name = faker.first_name() + str(faker.random_int())
# можно дату к имени
passw = faker.password()
print(name)
print(passw)

user_name = driver.find_element(by=By.ID, value="user-name")
user_name.send_keys(name)
password = driver.find_element(by=By.ID, value="password")
password.send_keys(passw)
