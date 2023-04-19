from time import sleep

import requests as requests
from bs4 import BeautifulSoup

def scrape(url):
    # set up headers
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    # set up proxies
    http_proxy = "http://10.10.1.10:3128"
    https_proxy = "https://10.10.1.11:1080"
    ftp_proxy = "ftp://10.10.1.10:3128"

    proxies = {
        "http" : http_proxy,
        "https" : https_proxy,
        "ftp" : ftp_proxy
    }

    # get the page of the product
    response = requests.get(url=url, headers=headers)
    contents = response.text
    print(contents)

    # Make soup
    soup = BeautifulSoup(contents, "html.parser")
    return soup


def selenium_scrape(html):
    # print(html)
    try:
        soup = BeautifulSoup(html, 'html.parser')
        print("try soup")
    except:
        soup = BeautifulSoup(html, 'lxml')
        print("execpt soup")
    print(soup)
    for item in soup.findAll(name="li"):
        for script in item.findAllNext(name="script"):
            if "url" in script.text:
                print("Url: " + script)

