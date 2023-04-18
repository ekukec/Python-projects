from undetected_chromedriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Google:
    def __init__(self) -> None:
        self.url = 'https://accounts.google.com/ServiceLogin'
        self.driver = Chrome(use_subprocess=True);
        self.driver.get(self.url)
        self.time = 10

    def login(self, email, password):
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(
            f'{email}\n')
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(
            f'{password}\n')

        self.code()

    def code(self):
        # [ ---------- paste your code here ---------- ]
        sleep(self.time)


#  ---------- EDIT ----------
email = 'test.testic02@gmail.com'  # replace email
password = 'Kea05gXM1RYCsCDdM6u'  # replace password
#  ---------- EDIT ----------

google = Google()
google.login(email, password)