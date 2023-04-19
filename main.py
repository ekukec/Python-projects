from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 30
PROMISED_UP = 5
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"

# Make instance of bot
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH, PROMISED_DOWN, PROMISED_UP, TWITTER_EMAIL, TWITTER_PASSWORD)

# Get the speed of the internet connection
bot.get_internet_speed()

# Login into the twitter account with the bot
bot.twitter_login()

# Start the main function of the bot
bot.tweet_at_provider()