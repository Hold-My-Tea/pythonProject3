
from datetime import datetime, timedelta
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://the-internet.herokuapp.com/key_presses?'
driver.get(base_url)
driver.maximize_window()

date_input = driver.find_element(By.XPATH, "//input[@id='target']")
""""Get now date"""
dt = datetime.now()
print(dt)

""""Get now date + 10 days"""
end_date = dt + \
                        timedelta(days = 10)
print(end_date)

""""Get now date + 10 days in proper format"""
end_date = end_date.strftime("%d.%m.%Y")
date_input.send_keys(end_date)
print(end_date)






# x_int = int(dt.strftime("%d%m%y"))
# print(x_int)
# new_date.clear()
# time.sleep(3)
# new_date.send_keys('08/06/2024')
# time.sleep(3)
# new_date.send_keys(Keys.RETURN)
# time.sleep(3)
# new_date.click()
# click_outside = driver.find_element(By.XPATH, "//div[@class='text-size-18 font-semibold px-10 py-10 text-black']")
# click_outside.click()
# new_date.click()
# date17 = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[7]/a")
# date17.click()
#
# current_date = datetime.utcnow().strftime("%d")
# print(current_date)
# date = int(current_date) + 1
# locator = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[7]/a")
#
# # login_standard_user = "standard_user"
# # password_all = "secret_sauce"
# # action = ActionChains(driver)
# # doubleclick = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
# # action.double_click(doubleclick).perform()
# #
# # right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
# # action.context_click(right_click).perform()
#
# # expand_button = driver.find_element(By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']")
# # expand_button.click()
#
#
# # if checkbox.is_selected():
# #     print("Чек-бокс выбран")
# # else:
# #     print("Чек-бокс не выбран")
# #
# # radiobutton1 = driver.find_element(By.XPATH, "//input[@value='rd1']")
# # radiobutton2 = driver.find_element(By.XPATH, "//input[@value='rd2']")
# # if radiobutton2.is_selected():
# #     print("Радиобатон2 выбран")
# # else:
# #     print("Радиобатон2 не выбран")
# #
# # radiobutton1.click()
# #
# # if radiobutton1.is_selected():
# #     print("Радиобатон1 выбран")
# # else:
# #     print("Радиобатон1 не выбран")
# #
# # radiobutton2 = driver.find_element(By.XPATH, "//input[@value='rd2']")
# # if radiobutton2.is_selected():
# #     print("Радиобатон2 выбран")
# # else:
# #     print("Радиобатон2 не выбран")
# #
# # # print('Input login')
# # # # time.sleep(3)
# # # # user_name.clear()
# # #
# # password = driver.find_element(By.XPATH, "//input[@id='password']")
# # password.send_keys(password_all)
# # print('Input password')
# # login_button = driver.find_element(by=By.ID, value="login-button")
# # login_button.click()
# # print('Click login button')
# #
# # # menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
# # # menu.click()
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