import requests
from bs4 import BeautifulSoup as b
import csv
fieldnames = ["Title" , "stock" , "price","rating"]
with open("books.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames= fieldnames)
    writer.writeheader()
for x in range(1,2):#adjust the range according to the number of pages you want to scrape
    url = "https://books.toscrape.com/catalogue/page-{}.html".format(x)
    response = requests.get(url)
    soup = b(response.text, "html.parser" )
    books = soup.find_all("h3")
    for book in books:
        url = "https://books.toscrape.com/catalogue/" + book.a["href"]
        response = requests.get(url)
        title = book.a["title"]
        if title:
            soup = b(response.text, "html.parser")
            stock  = soup.find("p", class_ = "instock availability").text.strip().split()[2].split("(")[1]
            price = soup.find("p", class_ = "price_color").text.strip().replace("Â£", "")
            rating = soup.find("p", class_ = "star-rating")["class"][1]
            data ={"Title" : title , "stock" : stock , "price" : price , "rating" : rating}
            with open("books.csv", "a", encoding="utf-8-sig",newline="") as f:
                writer = csv.DictWriter(f, fieldnames= fieldnames)
                writer.writerow(data)
        else :
            print("No title found for book at URL: {}".format(url))
    print("page {} done".format(x))
        