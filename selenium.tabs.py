

from faker import Faker
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://testpages.eviltester.com/styled/windows-test.html'


driver.get(base_url)
driver.maximize_window()

new_tab = driver.find_element(By.XPATH, "//a[@id='gobasicajax']")
new_tab.click()
print(driver.current_url)

header1 = driver.find_element(By.XPATH, "/html/body/div/h1")
value_1 = header1.text
print(value_1)
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)


header2 = driver.find_element(By.XPATH, "/html/body/div/h1")
value_2 = header2.text
print(value_2)

driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)