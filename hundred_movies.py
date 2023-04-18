from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

def hundred_movies_get():
    response = requests.get(url=url)
    contents = response.text

    soup = BeautifulSoup(contents, "html.parser")
    print(f"soup: {soup}")

    titles = [title.getText() for title in soup.findAll(name="h3", class_="title")]
    titles.reverse()
    print(f"titles: {titles}")

    file = open(file="movies.txt", mode="a", encoding="utf-8")
    for title in titles:
        file.write(title + "\n")
    file.close()

