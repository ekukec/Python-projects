from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class InternetSpeedTwitterBot:
    def __init__(self, chrome_path, promised_down, promised_up, username, password):
        # Make an instance of the webdriver so selenium can work
        self.driver = webdriver.Chrome(chrome_path)

        # Promised download speed in Mbps
        self.down = promised_down

        # Promised upload speed in Mbps
        self.up = promised_up

        # Username of the twitter profile the bot will use and log in to
        self.username = username

        # Password of the twitter profile the bot will use and log in to
        self.password = password

    # Gets the download and upload speed of the internet connection aswell as the internet provider name
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        try:
            WebDriverWait(self.driver,60).until(expected_conditions.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
            cookie_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            cookie_button.click()
        except:
            print("No cookie prompt")

        start = self.driver.find_element(By.CLASS_NAME, "start-text")
        start.click()

        WebDriverWait(self.driver, 300).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "result-container-speed-active")))
        results = self.driver.find_element(By.CLASS_NAME, "result-container-data")

        WebDriverWait(self.driver, 60).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "js-data-isp")))
        provider = self.driver.find_element(By.CLASS_NAME, "js-data-isp").text

        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "download-speed")))
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text

        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "upload-speed")))
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        data = {"provider" : provider,
                "download_speed" : download_speed,
                "upload_speed" : upload_speed}

        self.speed_test_data = data
        return data

    # Tweets at the provider using the speed test data acquired with the get_internet_speed_function
    def tweet_at_provider(self):


        tweet = f"{self.speed_test_data['provider']} why is my internet speed {self.speed_test_data['download_speed']}down/{self.speed_test_data['upload_speed']}up\n" \
                f"when it is supposed to be {self.down}down/{self.up}up?"

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "public-DraftStyleDefault-block")))
        tweet_input = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        tweet_input.click()
        tweet_input.send_keys(tweet)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')))
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(10)

    # Logins into the twitter account using the data contained in the properties username and password
    def twitter_login(self):
        self.driver.get("https://twitter.com/i/flow/login")

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "text")))
        username_input = self.driver.find_element(By.NAME, "text")
        username_input.send_keys(self.username, Keys.ENTER)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "password")))
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(self.password, Keys.ENTER)