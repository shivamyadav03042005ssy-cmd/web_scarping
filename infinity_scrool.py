import time
from playwright.sync_api import sync_playwright,TimeoutError
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto("https://www.scrapingcourse.com/infinite-scrolling", wait_until="domcontentloaded", timeout=20000)
    attempts = 0
    for x in range(1,50):#adjust according to requirement
        try:
            name = page.locator(".product-name").nth(x).inner_text(timeout=4000)
            rate = page.locator(".product-price.text-slate-600").nth(x).inner_text(timeout=4000)
            print(name)
            print(rate)
            print("-"*50)
            print(x)
        except TimeoutError:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            try:
                name = page.locator(".product-name").nth(x).inner_text(timeout=3000)
                rate = page.locator(".product-price.text-slate-600").nth(x).inner_text(timeout=3000)
                print(name)
                print(rate)
                print("-"*50)
            except TimeoutError:
                print("sara data khatam")
                break
