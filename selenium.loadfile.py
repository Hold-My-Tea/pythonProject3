import time


from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.maximize_window()

pass_upload = "C:\\Users\\Oksana\\AQA\\pythonProject3\\screen\\download.jpg"
click_button = driver.find_element(By.XPATH, "//input[@id='file']")
click_button.send_keys(pass_upload)
print("click_button")
time.sleep(3)
