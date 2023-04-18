from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

article_button = driver.find_element(By.XPATH, "//a[@title='Special:Statistics']")

# print(article_button.text)
# article_button.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Pages")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)