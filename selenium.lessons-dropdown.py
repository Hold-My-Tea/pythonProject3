import time

from pycparser.c_ast import Return
from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# base_url = 'https://www.saucedemo.com/'
#
# # Open browser
# driver.get(base_url)
# # Maximize window
# driver.maximize_window()
# #Freeze for sometime
# # time.sleep(10)
# # Close browser
# # driver.close()
#
# # user_name = driver.find_element(by=By.ID, value="user-name")
# # # user_name.send_keys("standard_user")
# password = driver.find_element(by=By.ID, value="password")
# password.send_keys("secret_sauce")
# login_button = driver.find_element(by=By.ID, value="login-button")
#
#
# # by xpath
# user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
# user_name.send_keys("standard_user")
#
# login_button.click()
#
#
# # # refresh page
# # driver.refresh()
#
# select = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
# # select.select_by_visible_text('Name (Z to A)')
# select.select_by_value('za')



base_url = 'https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.maximize_window()


click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop.click()
print('Click dropdown')
time.sleep(3)
# click_country = driver.find_element(By.XPATH, "//li[@class='select2-results__option'][3]")
# click_country.click()
# print('Click country')

click_empty = driver.find_element(By.XPATH, "(//input[@class='select2-search__field'])[2]")
click_empty.send_keys('denmark')
time.sleep(3)
click_empty.send_keys(Keys.RETURN)