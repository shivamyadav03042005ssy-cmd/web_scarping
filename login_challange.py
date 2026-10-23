import requests
url ="https://www.scrapingcourse.com/login"
dashboard_url = "https://www.scrapingcourse.com/dashboard"
payload ={"email": "admin@example.com", "password":"password"}
with requests.session() as s:
    s.headers.update({"useragent": "mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
    print("attempting login..")
    login_reponse = s.post(url , data = payload)
    print("navigation to dashboard..")
    dashboard_reponse = s.get(dashboard_url)
    if "Welcome" in dashboard_reponse or "product" in dashboard_reponse.text.lower():
        print(dashboard_reponse.text)
        print("login succesfully")
    else :
        print("login falled")