import time


from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.maximize_window()

iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)

input_field = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]")
value_input_field = input_field.text
print(value_input_field)

input_field.send_keys(Keys.CONTROL + 'a')
editing_panel = driver.find_element(By.XPATH, "//button[@class='rsw-btn']")
editing_panel.click()
print('editing_panel')

locate_bold = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/b")
value_locate_bold = locate_bold.text
print(value_locate_bold)
assert value_input_field == value_locate_bold
print('True')