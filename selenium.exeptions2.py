import time

from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

# try:
#     vis_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     vis_button.click()
# except NoSuchElementException as exception:
#     print('NoSuchElementException')
#     time.sleep(7)
#     vis_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     vis_button.click()
#     print('Click vis button')
# # print("click_button")

yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_checkbox.click()
try:
    massage = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = massage.text
    print(value_message)
    assert value_message == 'No'
except AssertionError as exception:
    driver.refresh()
    yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_checkbox.click()
    massage = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = massage.text
    print(value_message)
    assert value_message == 'Yes'
    print('Checkbox yes')