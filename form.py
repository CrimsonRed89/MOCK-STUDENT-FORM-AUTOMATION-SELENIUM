from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys
import csv

path = "C:\\Coding1\\Coding\\python\\Automation\\chromedriver-win64\\chrome.exe"

url = "https://www.techlistic.com/p/selenium-practice-form.html"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\aayus\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\Default")
options.add_argument("profile-directory=Default") 
options.binary_location = path

driver = webdriver.Chrome(options)
driver.get(url)

driver.execute_script("window.scrollBy(0, 900);")

firstname = driver.find_element(By.CSS_SELECTOR, "input[name='firstname']")
firstname.click()
firstname.send_keys("Aayush")

lastname = driver.find_element(By.CSS_SELECTOR, "input[name='lastname']")
lastname.click()
lastname.send_keys("Arora")

gender_button = driver.find_element(By.CSS_SELECTOR, "input[id='sex-0']")
gender_button.click()

experience = driver.find_element(By.CSS_SELECTOR, "input[id='exp-0']")
experience.click()

driver.execute_script("window.scrollBy(0, 300);")

date = driver.find_element(By.CSS_SELECTOR, "input[id='datepicker']")
date.click()
date.send_keys("29-09-2024")

profession = driver.find_element(By.CSS_SELECTOR, "input[id='profession-0']")
profession.click()

tools = driver.find_element(By.CSS_SELECTOR, "input[id='tool-2']")
tools.click()

driver.execute_script("window.scrollBy(0, 300);")

continent = driver.find_element(By.CSS_SELECTOR, "select[id='continents']")
continent.click()
continent.send_keys(Keys.RETURN)
time.sleep(0.5)

select_element = driver.find_element(By.CSS_SELECTOR, "select[id='selenium_commands']")
select_element.click()
select_element.send_keys(Keys.ARROW_DOWN * 4)

file_input = driver.find_element(By.CSS_SELECTOR, "input[id='photo']")
file_input.send_keys("C:\\Coding1\\Coding\\python\\Automation\\Automation_Mock_form\\steam.jpeg")
time.sleep(1)

driver.execute_script("window.scrollBy(0, -300);")
driver.execute_script("window.scrollBy(0, -300);")

action = ActionChains(driver)

driver.execute_script("document.body.style.zoom='50%'")

driver.execute_script("window.scrollBy(0, -300);")
driver.execute_script("window.scrollBy(0, -300);")

submit = driver.find_element(By.CSS_SELECTOR, "button[id='submit']")
submit.click()

driver.quit()




