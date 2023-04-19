from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

LINKEDIN_EMAIL = "YOUR EMAIL"
LINKEDIN_PASSWORD = "YOUR PASSWORD"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs")

sign_in_button1 = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in_button1.click()

username = driver.find_element(By.NAME, "session_key")
username.send_keys(LINKEDIN_EMAIL, Keys.ENTER)

password = driver.find_element(By.NAME, "session_password")
password.send_keys(LINKEDIN_PASSWORD, Keys.ENTER)

sleep(10)

