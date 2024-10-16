import time


from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.maximize_window()
#
# mess = "standard_user"
# input_field = driver.find_element(By.XPATH, "//input[@id='user-message']")
# input_field.send_keys(mess)
#
# get_value = driver.find_element(By.XPATH, "//button[@id='showInput']")
# get_value.click()
#
# your_message = driver.find_element(By.XPATH, "//p[@id='message']")
# assert your_message.text == mess
# print('True')
# ################################################################################
mess1 = 22
input_field1 = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_field1.send_keys(mess1)

mess2 = 11
input_field2 = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_field2.send_keys(mess2)

get_value = driver.find_element(By.XPATH, "//button[contains(text(), 'Get Sum')]")
get_value.click()

num = mess1+mess2
your_message = driver.find_element(By.XPATH, "//p[@id='addmessage']")
assert your_message.text == str(num)
print('True')