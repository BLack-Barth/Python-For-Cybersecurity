from playwright.sync_api import sync_playwright
from rich import print

payloads = [
    "%7C",
    "%27",
    "//*",
    "||'6",
    "*/*",
    "%27",
    "%%2727",
    "%25%27"
]
base_url = "http://testaspnet.vulnweb.com/Comments.aspx?id=2"

with sync_playwright() as spr:
    browser = spr.firefox.launch(headless=True)
    page = browser.new_page()
    page.goto(base_url)
    first_code_html = page.text_content('body')
    for payload in payloads:
        query = f"{base_url}{payload}"
        page.goto(query)
        second_code_html = page.text_content('body')
        if first_code_html != second_code_html:
            print(f"[green]SQL injection detected[/]:{query}")
            print(second_code_html)
        else:
            pass
    browser.close()