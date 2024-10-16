import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from OOP.login_page import LoginPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Test1:
    def test_select_product(self):
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(5)
        self.ff = bool

        print('Start test')

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        login = LoginPage(driver)
        login.authorization(login_name = login_standard_user, login_password = password_all)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print('Select product')
        cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                     "//a[@class='shopping_cart_link']")))
        cart.click()
        print('Click cart button')

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                     "//span["
                                                                                     "@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print('True')

        time.sleep(10)

test = Test1()
test.test_select_product()


class CarTest1()