# import requests

# from bs4 import BeautifulSoup as b
# for x in range(1,3):
#     url = "https://quotes.toscrape.com/page/{page}/".format(page = x)
#     response = requests.get(url)
#     soup = b(response.text, "html.parser")
#     l = len(soup.find_all("span", class_ = "text"))
#     for x in range(1, l+1):
#         quotes = soup.find_all("span", class_ = "text")[x-1]
#         by = soup.find_all("small", class_ = "author")[x-1]
#         with open ("quotes.txt","a", encoding="utf-8-sig") as f:
#             f.write(quotes.text)
#             f.write("\n")
#             f.write(by.text)
#             f.write("\n")


import os
from playwright.sync_api import sync_playwright
base_url = "https://quotes.toscrape.com/"
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    for x in range(1,3):
        page.goto(base_url+f"page/{x}/")
        quotes = page.locator(".quote")
        for quote in quotes.all():
            text = quote.locator(".text").inner_text()
            author = quote.locator(".author").inner_text()
            tags = quote.locator("a.tag").all_inner_texts()
            with open("quote.txt","a",encoding='utf-8') as f:
                f.write(f"quote:{text}\n")
                f.write(f"author{author}\n")
                f.write(f"Tags{tags}\n")
                s ="-"*50
                f.write(f"{s}\n")
                