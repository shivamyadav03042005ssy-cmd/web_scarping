# import time 
# from playwright.sync_api import sync_playwright
# #from playwright_stealth import Stealth
# target_url = "https://www.scrapingcourse.com/antibot-challenge"
# with sync_playwright() as p:
#     context = p.chromium.launch_persistent_context(user_data_dir="./cus",channel="chrome",headless= False ,no_viewport= True)#,ignore_default_args=['--enable-automation'],args= ["--disable-blink-features=AutomationControlled","--start-maximized"],user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
#     #context = browser.new_context(viewport={"width":1280,"height":720}, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
#     page = context.pages[0]
#     #Stealth().apply_stealth_sync(page)
#     # try :
#     page.goto(target_url)
#     page.wait_for_timeout(15000)
#     try:
#         iframe_element =page.wait_for_selector("iframe[src*='://cloudflare.com']",timeout = 20000)
#         box = iframe_element.bounding_box()
#         page.mouse.move(box["x"]+20,box['y']+20,steps=15)
#         page.mouse.click(box["x"]+30,box["y"]+box["height"]/2)
#     except Exception:
#         print("shit")
#         # challenge_frame = iframe_element.content_frame()
#         # print("clicking turnstile checkbox")
#         # challenge_frame.click('input[type ="checkbox"],#challenge-stage , .mark' , timeout=5000)
#     page.wait_for_selector("body",timeout=30000)
#     time.sleep(10)
#     print("win")
#     print("page tittle:",page.title())
#     html_content = page.content()
#     print(html_content[:500])
#     s =input(":")
#     # except Exception as e:
#     #     print("losed")
#     # finally :
#     #     browser.close()
import asyncio
import nodriver as uc

async def main ():
    url = "https://www.scrapingcourse.com/antibot-challenge"
    browser = await uc.start()
    page = await browser.get(url)
    await asyncio.sleep(50)
    print(await page.evaluate("document.title"))
    print( await)
    html = await page.get_content()
    print(html[:500])
    input("enter to stop the browser:")
    browser.stop()
asyncio.run(main())