#----------------------------------------PROJECT------------------------------------------------
from bs4 import BeautifulSoup
import requests


for i in range(1, 51):

    title_selector = ".product_pod h3 a"
    rating_selector = ".star-rating"    
    price_selector = ".price_color"

    urf = f"http://books.toscrape.com/catalogue/category/books_1/page-{i}.html"

    data = requests.get(urf).content
    soup = BeautifulSoup(data, "html.parser")

    rating_map = {
        "One" : "★",
        "Two" : "★ ★",
        "Three" : "★ ★ ★",
        "Four" : "★ ★ ★ ★",
        "Five" : "★ ★ ★ ★ ★"
    }


    titles = soup.select(title_selector)
    ratings = soup.select(rating_selector)
    prices = soup.select(price_selector)

    def get_rating(tag):
        for term, rating in rating_map.items():
            if term in tag["class"]:
                return rating
        

    with open("WorkingOnYourOwn/WebScraping/book.csv", mode= "a", encoding= "utf-8") as book_file:
        for title, price, rating in zip(titles, prices, ratings):
            book_file.write(f"{title['title']}, {price.string}, {get_rating(rating)}\n")

# DONE