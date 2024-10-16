import time

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

###Login process
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):

        ### user info
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                  "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print('Input login')

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   "//input[@id='password']")))
        password.send_keys(login_password)
        print('Input password')
        ### Login button
        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   "//input[@id='login-button']")))
        login_button.click()
        print('Click login button')

        ### Exceptions
        try:
            text_products = driver.find_element(By.XPATH, "//span[@class='title']")
            value_text_products = text_products.text
            assert value_text_products == 'Products'
            print('Authorization success')
        except NoSuchElementException:
            print("Authorization failed")

        time.sleep(3)

        try:
            menu = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                              "@id='react-burger-menu-btn']")))
            menu.click()

            logout_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                                             "//a["
                                                                                             "@id='logout_sidebar_link']")))
            logout_button.click()
        except TimeoutException:
            print("Element is not found")
            driver.refresh()




### Collect user details
class Test1:
    def test_with_users(self, log):
        time.sleep(3)

        password_all = "secret_sauce"

        login = LoginPage(driver)
        login.authorization(login_name = log, login_password = password_all)

### List of users
list_users = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]

### Login for all users in list
for i in list_users:
    print(f'Start test with user {i}')
    test = Test1()
    test.test_with_users(i)
    print(f'Test with user {i} is okay')





