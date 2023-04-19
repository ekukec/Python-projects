from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fake_useragent import UserAgent

from dataclasses import dataclass

# Data structure for price
@dataclass
class Price:
    minimum: int
    maximum: int

# Data structure for beds and bathrooms
@dataclass
class Beds:
    beds: str
    bathroom: str

# Data structure for home type
@dataclass
class HomeType:
    houses: bool
    multi_family: bool
    townhomes: bool
    condos: bool
    lots: bool
    apartments: bool
    manufactured: bool

class ZillowBot:
    def __init__(self, chrome_path, options):
        # Make an instance of the webdriver so selenium can work
        if options:
            options = webdriver.ChromeOptions()
            ua = UserAgent()
            userAgent = ua.random
            options.add_argument(f'user-agent={userAgent}')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--headless')
            options.add_argument('window-size=1920x1080')
            self.driver = webdriver.Chrome(chrome_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome(chrome_path)


    # Finds the properties which fulfill the desired requirements passed in the function arguments
    def find_properties(self, location, listing_type, price :Price, beds :Beds, home_type :HomeType, more):
        self.driver.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56293333959961%2C%22east%22%3A-122.30372466040039%2C%22south%22%3A37.69125507932883%2C%22north%22%3A37.859232413339626%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")

        # Enters the desired location
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID,"srp-search-box")))
        search_box = self.driver.find_element(By.ID, "srp-search-box")
        location_input = search_box.find_element(By.TAG_NAME, "input")
        location_input.send_keys(location)


        # Chooses the desired listing type
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "listing-type")))
        listing_type_input = self.driver.find_element(By.ID, "listing-type")
        listing_type_input.click()

        match listing_type:
            case "sale":
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "isForSaleByAgent_isForSaleByOwner_isNewConstruction_isComingSoon_isAuction_isForSaleForeclosure_isPreMarketForeclosure_isPreMarketPreForeclosure")))
                button = listing_type_input.find_element(By.ID, "isForSaleByAgent_isForSaleByOwner_isNewConstruction_isComingSoon_isAuction_isForSaleForeclosure_isPreMarketForeclosure_isPreMarketPreForeclosure")
                button.click()
            case "rent":
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "isForSaleByAgent_isForSaleByOwner_isNewConstruction_isComingSoon_isAuction_isForSaleForeclosure_isPreMarketForeclosure_isPreMarketPreForeclosure")))
                button = listing_type_input.find_element(By.ID, "isForRent")
                button.click()
            case "sold":
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "isRecentlySold")))
                button = listing_type_input.find_element(By.ID, "isRecentlySold")
                button.click()

        listing_type_input.click()


        # Chooses the desired price range
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "price")))
        price_input = self.driver.find_element(By.ID, "price")
        price_input.click()


        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/div/section/div[2]/div/div[2]/section/div/div/form/div/fieldset/div/div[1]/div/div/div/input")))
        price_input_min = price_input.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/section/div[2]/div/div[2]/section/div/div/form/div/fieldset/div/div[1]/div/div/div/input")
        price_input_min.click()
        sleep(1)
        price_input_min.send_keys(str(price.minimum))
        sleep(1)

        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[5]/div/section/div[2]/div/div[2]/section/div/div/form/div/fieldset/div/div[2]/div/div/div/input")))
            price_input_max = price_input.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/section/div[2]/div/div[2]/section/div/div/form/div/fieldset/div/div[2]/div/div/div/input")
            price_input_max.click()
            sleep(1)
            price_input_max.send_keys(Keys.LEFT_CONTROL + "a")
            sleep(1)
            price_input_max.send_keys(str(price.maximum))
        except:
            print("couldnt enter price max")


        # Chooses the desired bed and bathroom requirements
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "beds")))
        beds_input = self.driver.find_element(By.ID, "beds")
        beds_input.click()
        sleep(1)
        beds_input.click()

        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, "beds-options")))
        beds_option = beds_input.find_element(By.NAME, "beds-options")
        beds_option_buttons = beds_option.find_elements(By.TAG_NAME, "button")
        match beds.beds.lower():
            case "any":
                beds_option_buttons[0].click()
            case "1+":
                beds_option_buttons[1].click()
            case "2+":
                beds_option_buttons[2].click()
            case "3+":
                beds_option_buttons[3].click()
            case "4+":
                beds_option_buttons[4].click()
            case "5+":
                beds_option_buttons[5].click()

        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, "baths-options")))
        baths_option = beds_input.find_element(By.NAME, "baths-options")
        baths_option_buttons = baths_option.find_elements(By.TAG_NAME, "button")
        match beds.beds.lower():
            case "any":
                baths_option_buttons[0].click()
            case "1+":
                baths_option_buttons[1].click()
            case "1.5+":
                baths_option_buttons[2].click()
            case "2+":
                baths_option_buttons[3].click()
            case "3+":
                baths_option_buttons[4].click()
            case "4+":
                baths_option_buttons[5].click()

        beds_input.click()


        # Chooses the desired type of home
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "home-type")))
        home_type_input = self.driver.find_element(By.ID, "home-type")
        home_type_input.click()

        if home_type.houses:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "home-type_isSingleFamily")))
            houses_button = home_type_input.find_element(By.ID, "home-type_isSingleFamily")
            houses_button.click()
        if home_type.townhomes:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "home-type_isTownhouse")))
            townhomes_button = home_type_input.find_element(By.ID, "home-type_isTownhouse")
            townhomes_button.click()
        if home_type.multi_family:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "home-type_isMultiFamily")))
            multi_family_button = home_type_input.find_element(By.ID, "home-type_isMultiFamily")
            multi_family_button.click()
        if home_type.condos:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "home-type_isCondo")))
            condos_button = home_type_input.find_element(By.ID, "home-type_isCondo")
            condos_button.click()
        if home_type.lots:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "home-type_isLotLand")))
            lots_button = home_type_input.find_element(By.ID, "home-type_isLotLand")
            lots_button.click()
        if home_type.apartments:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "home-type_isApartment")))
            apartments_button = home_type_input.find_element(By.ID, "home-type_isApartment")
            apartments_button.click()
        if home_type.manufactured:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "home-type_isManufactured")))
            manufactured_button = home_type_input.find_element(By.ID, "home-type_isManufactured")
            manufactured_button.click()

        # WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "more")))
        # more_input = self.driver.find_element(By.ID, "more")
        # more_input.send_keys()

        return self.driver.page_source

    # Gets page source using headless mode
    def get_page_source(self):
        self.driver.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56293333959961%2C%22east%22%3A-122.30372466040039%2C%22south%22%3A37.69125507932883%2C%22north%22%3A37.859232413339626%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")
        # WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID, "search-page-list-container")))
        # search_page = self.driver.find_element(By.ID, "search-page-list-container")
        # search_page.click()
        #
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", search_page)
        sleep(1)

        return self.driver.page_source
