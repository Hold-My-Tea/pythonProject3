import time

from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/dynamic-properties'
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

