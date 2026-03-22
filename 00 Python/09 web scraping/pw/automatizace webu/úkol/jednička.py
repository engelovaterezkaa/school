from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
passwd = getenv("PASSWORD")

prg = 'a.aalink coursename mr-2 mb-1'

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")

        page.click('span.login.pl-2') 

        page.fill('input#username', login)

        page.fill('input#password', passwd)

        page.click('button#loginbtn')

        page.goto("https://www.moodle-trebesin.cz/course/view.php?id=277")



        # page.locator('span.instancename').locator(":has-text('Úkol jednička? ')").click()
        page.locator("span.instancename:has-text('Úkol jednička?')").click() #locator automaticky nečeká ale click ano

        page.click('a.btn-primary')
        page.fill('input#id_subject', "Jednička")
   
        frame = page.frame_locator('#id_message_ifr')
        editor  = frame.locator('body')
        editor.fill('Dáte mi prosím jedničku? :3')
        page.click('input#id_submitbutton')

        input("gfkdshbgkb")
        browser.close()

if __name__ == "__main__":
    main()