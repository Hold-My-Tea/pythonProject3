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

base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()

# login_standard_user = "standard_user"
# password_all = "secret_sauce"
checkbox = driver.find_element(By.XPATH, "//input[@value='cb1']")
checkbox.click()

# expand_button = driver.find_element(By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']")
# expand_button.click()


if checkbox.is_selected():
    print("Чек-бокс выбран")
else:
    print("Чек-бокс не выбран")

radiobutton1 = driver.find_element(By.XPATH, "//input[@value='rd1']")
radiobutton2 = driver.find_element(By.XPATH, "//input[@value='rd2']")
if radiobutton2.is_selected():
    print("Радиобатон2 выбран")
else:
    print("Радиобатон2 не выбран")

radiobutton1.click()

if radiobutton1.is_selected():
    print("Радиобатон1 выбран")
else:
    print("Радиобатон1 не выбран")

radiobutton2 = driver.find_element(By.XPATH, "//input[@value='rd2']")
if radiobutton2.is_selected():
    print("Радиобатон2 выбран")
else:
    print("Радиобатон2 не выбран")

# print('Input login')
# # time.sleep(3)
# # user_name.clear()
#
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print('Input password')
# login_button = driver.find_element(by=By.ID, value="login-button")
# login_button.click()
# print('Click login button')
#
# # menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
# # menu.click()
# # print('Click menu button')
# # time.sleep(3)
# #
# # link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
# # link_about.click()
# # print('Click link button')
# # url = 'https://saucelabs.com/'
# # get_url = driver.current_url
# # print(get_url)
# # assert url == get_url
# # print('True')
# # time.sleep(3)
# driver.back()
# print('Go back')
# time.sleep(3)
# driver.forward()
# print('Go forward')