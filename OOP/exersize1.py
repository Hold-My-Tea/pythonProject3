import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from test1 import driver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Test1:
    def test_1(self):
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()



class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):

        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                  "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print('Input login')

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   "//input[@id='password']")))
        password.send_keys(login_password)
        print('Input password')

        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   "//input[@id='login-button']")))
        login_button.click()
        print('Click login button')

        menu = self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
        menu.ckick()

        logout_button = self.driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
        logout_button.click()

login_standard_user = "standard_user"
password_all = "secret_sauce"

login = LoginPage(driver)
login.authorization(login_standard_user, password_all)

test = Test1()
test.test_1()

        # try:
        #     result = num_1 / num_2
        #     print(f"Результат деления: {result}")
        # except ZeroDivisionError:
        #     print("На ноль делить нельзя")