from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class InstagramFollowerBot:
    def __init__(self, chrome_path, target_account, username, password):
        # Make an instance of the webdriver so selenium can work
        self.driver = webdriver.Chrome(chrome_path)

        # The username of the target instagram account
        self.instagram_account = target_account

        # The username of the instagram profile the bot will use and log in to
        self.username = username

        # The password of the instagram profile the bot will use and log in to
        self.password = password

    # Follows the followers of the targeted account contained in the propety instagram_account
    def follow_target_followers(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div")))
        followers_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div")
        followers_button.click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')))
        followers_popup = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')

        sleep(3)
        followers_list = followers_popup.find_elements(By.TAG_NAME, "button")
        previous_len = 0
        while len(followers_list) != previous_len:
            print(f"num of buttons: {len(followers_list)}")

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            sleep(3)
            previous_len = len(followers_list)
            followers_list = followers_popup.find_elements(By.TAG_NAME, "button")

        print("finished loading followers")

        for button in followers_list:
            if button.text.lower() == "follow":
                button.click()


    # Follows the instagram account contained in the property instagram_account
    def follow_target_account(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button")))
        follow_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button")
        follow_button.click()
        sleep(10)

    # Finds the instagram account contained in the property instagram_account
    def find_target_account(self):
        # WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_WI"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')))
        # not_now_button = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_WI"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        # not_now_button.click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/a/div/div/div/div')))
        search_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/a/div/div/div/div')
        search_button.click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "_aauy")))
        search_bar = self.driver.find_element(By.CLASS_NAME, "_aauy")
        search_bar.send_keys(self.instagram_account, Keys.ENTER)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/div[1]")))
        target_account = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/div[1]")

        if target_account.text == self.instagram_account:
            target_account.click()
        else:
            print("Account not found!")
            self.driver.quit()

    def instagram_login(self):
        self.driver.get("https://www.instagram.com/")

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "_a9_1")))
        cookie_button = self.driver.find_element(By.CLASS_NAME, "_a9_1")
        cookie_button.click()

        sleep(3)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "username")))
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(self.username)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "password")))
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(self.password, Keys.ENTER)

