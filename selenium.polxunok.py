import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'

# Open browser
driver.get(base_url)
# Maximize window
driver.maximize_window()

action = ActionChains(driver)

default = driver.find_element(By.XPATH, "//*[@id='slidecontainer']/input")
action.click_and_hold(default).move_by_offset(20, 0).release().perform()
time.sleep(3)
action.click_and_hold(default).move_by_offset(0, 0).release().perform()