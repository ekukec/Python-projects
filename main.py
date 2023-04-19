from time import sleep

from InstagramFollowerBot import InstagramFollowerBot

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
INSTAGRAM_EMAIL = "YOUR EMAIL"
INSTAGRAM_PASSWORD = "YOUR PASSWORD"
TARGET_ACCOUNT = "ACCOUNT U WISH TO GET THE FOLLOWERS FROM"

# Make an instance of bot
bot = InstagramFollowerBot(CHROME_DRIVER_PATH, TARGET_ACCOUNT, INSTAGRAM_EMAIL, INSTAGRAM_PASSWORD)

# Log in with the bot
bot.instagram_login()
sleep(10)

# Find target account
bot.find_target_account()
sleep(5)

# Follow the target account
bot.follow_target_account()

# Follow the followers of the target account
bot.follow_target_followers()
sleep(300)