from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
passwd = getenv("PASSWORD")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")

        #page.click('span[class="login pl-2"]')
        page.click('span.login.pl-2') #-->CSS zápis

        #page.fill('input[id="username"]', "engelova122")
        page.fill('input#username', login)

        page.fill('input#password', passwd)

        page.click('button#loginbtn')

        input("Zmáčkni klávesu na zavření prohlížeče")
        browser.close()

if __name__ == "__main__":
    main()