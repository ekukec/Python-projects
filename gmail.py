from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc



options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = uc.Chrome(use_subprocess=True)

url = "https://accounts.google.com/v3/signin/identifier?dsh=S335807938%3A1678301367762108&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHcscDB9KuM0ZjEZfdHtR3hg09ynTtABi3S_SJLw7hWBXSljFLl_f_xt-Xrk3laT4czqyYSPqw"
driver.get(url)

email = driver.find_element(By.NAME, "identifier")
email.send_keys("test.testic02@gmail.com", Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)

try:
    wait = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "Passwd")))
    password = driver.find_element(By.NAME, "Passwd")
    password.send_keys("Kea05gX8M1RYCsCDdM6u", Keys.TAB, Keys.TAB, Keys.ENTER)
    sleep(10)
finally:
    driver.quit()
