from time import sleep

import requests as requests
from bs4 import BeautifulSoup

def scrape(url):
    # set up headers
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(
        url,
        headers=header)

    data = response.text
    soup = BeautifulSoup(data, "html.parser")

    return soup

def get_links(soup):
    all_link_elements = soup.select("a.property-card-link[tabindex='0']")
    # print(all_link_elements)
    all_links = []

    for link in all_link_elements:
        href = link["href"]
        if "http" not in href:
            all_links.append(f"https://www.zillow.com{href}")
        else:
            all_links.append(href)

    return all_links

def get_addresses(soup):
    all_address_elements = soup.select("address")
    all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

    return all_addresses

def get_prices(soup):
    all_price_elements = soup.select("span[data-test='property-card-price']")
    # print(all_price_elements)
    all_prices = [price_el.text.split("+")[0] if "+" in price_el.text else price_el.text.split("/")[0] for price_el in all_price_elements]

    return all_prices