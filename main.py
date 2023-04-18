import smtplib
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

email = "test.testic02@gmail.com"

# function which sends the mail to user if the price is lower or equal to the benchmark price
def notify_user(send_to, product_name, product_price, product_url):
    MY_EMAIL = "test.testic02@gmail.com"
    MY_PASSWORD = "dmolfoonjjqsiapl"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        message = 'Subject: Amazon price alert\n\n' + f'Get the {product_name} for the low price of {product_price}\n\nClick this link to go and buy the product: {product_url}'

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=send_to,
            msg=message.encode('utf-8'))



# url of the product we want to track the price of
url="https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=pd_rhf_d_ee_s_pd_sbs_rvi_sccl_1_1/135-0460176-6142851?pd_rd_w=ajYm2&content-id=amzn1.sym.a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_p=a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_r=DXMH2P11MG8EBAPZ060P&pd_rd_wg=ODUOg&pd_rd_r=4efb55e1-73cd-402a-8f9f-cd8ae7ccb159&pd_rd_i=B06Y1MP2PY&th=1"

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
# response = urlopen(url=url)
# contents = response.read()

# make soup and find the price and product name
soup = BeautifulSoup(contents, "html.parser")
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
product_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText()

# get price in float format
product_price = float(price_whole) + float(price_fraction) / 100

# set up price which you are willing to pay
my_price = 125.55

if product_price <= my_price:
    notify_user(email, product_name, product_price, url)

print(f"product price: {product_price}")
