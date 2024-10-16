import glob
import os
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()

path_to = "C:\\Users\\Oksana\\AQA\\pythonProject3\\screen\\"
prefs = {'download.default_directory' : path_to}


options.add_experimental_option("detach", True)
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.maximize_window()


click_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
click_button.click()
print("click_button")

# # Директория не пустая
# if os.listdir(path_to):
#     print('True')
# else:
#     print('False')
#
# # Вывести содержимое директории списком
# print(os.listdir(path_to))

# Наличие файла в директории
file_name = 'LambdaTest.pdf'
file_path = path_to + file_name
assert os.access(file_path, os.F_OK) == True
print('True')
time.sleep(3)
# Файл не пуст
# files = glob.glob(os.path.join(path_to, "*.*"))
# for file in files:
#     a = os.path.getsize(file)
#     if a > 10:
#         print("File is not empty")
#     else:
#         print("File is empty")

# Delete file
files = glob.glob(os.path.join(path_to, "*.*"))
for file in files:
     os.remove(file)