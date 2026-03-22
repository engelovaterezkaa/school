from playwright.sync_api import sync_playwright
import random 

login = "hokuspokus"
passwd = "hokuspokus"

random_no = random.randint(0,100)

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

        page.locator("span.instancename:has-text('Hokus pokus zpráva')").click()

        page.goto("https://www.moodle-trebesin.cz/mod/forum/discuss.php?d=515")

        # page.goto("https://www.moodle-trebesin.cz/mod/forum/post.php?reply=1079#mformforum")
   
        # frame = page.frame_locator('#id_message_ifr')
        # editor  = frame.locator('body')
        # editor.fill(str(random_no))
        # page.click('input#id_submitbutton')

        article1103 = page.locator('article#p1103')
        article1103.click()

        input("gfkdshbgkb")
        browser.close()

if __name__ == "__main__":
    main()