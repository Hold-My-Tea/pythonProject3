import time


from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.maximize_window()


alert1 = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
alert1.click()
print("alert1")
time.sleep(3)

driver.switch_to.alert.accept()


alert2 = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
alert2.click()
print("alert2")
time.sleep(3)

driver.switch_to.alert.dismiss()