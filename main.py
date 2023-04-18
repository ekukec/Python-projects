from bs4 import BeautifulSoup
import requests
import hundred_movies

url = "https://news.ycombinator.com/news"

response = requests.get(url)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

articles = soup.findAll(name="span", class_="titleline")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.find(name="a").get("href"))
article_upvotes = [int(article.getText().split(sep=' ')[0]) for article in soup.findAll(name="span", class_="score")]

print(f"ar txt: {article_texts}\nar links: {article_links}\nar upv: {article_upvotes}")

ar_zip = zip(article_upvotes, article_texts, article_links)
# for item in ar_zip:
#     print(item)

ar_zip_sorted = sorted(ar_zip, reverse=True)
# for item in ar_zip_sorted:
#     print(item)

ar_unzip = zip(*ar_zip_sorted)
# for item in ar_unzip:
#     print(item)

# ar_unzip_list = map(list, ar_unzip)
# for item in ar_unzip_list:
#     print(item)

list_ar1, list_ar2, list_ar3 = map(list, ar_unzip)
# print(f"{list_ar1}\n{list_ar2}\n{list_ar3}")

l1,l2,l3 = map(list, zip(*sorted(zip(article_upvotes, article_texts, article_links), reverse=True)))
# print(f"{l1}\n{l2}\n{l3}")

hundred_movies.hundred_movies_get()

# import lxml
#
# with open("website.html") as doc:
#     contents = doc.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# print(soup.title)
# print(soup.title.string)
#
# findall = soup.findAll(name="a")
# print(findall)
#
# for tag in findall:
#     print(tag.getText())
#     print(tag.get("href"))
#
# h1_name = soup.find(name="h1", id="name")
# print(h1_name)
#
# h3_class = soup.findAll(name="h3", class_="heading")
# print(h3_class)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name_select = soup.select_one(selector="#name")
# print(name_select)
#
# class_select = soup.select(".heading")
# print(class_select)