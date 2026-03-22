from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.arsenal.com/results"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    other_score = int(soup.select_one(".scores__score").get_text(strip=True)) #span
    arsenal_score = int(soup.select_one(".scores__score.scores__score--arsenal").get_text(strip=True))

    def mood():
        if arsenal_score > other_score:
            print("happy jak dva grepy :)")
        elif arsenal_score == other_score:
            print("buy coffee just to be sure :/")
        else: 
            print("run :0")

    mood()

    team = soup.select_one(".team-crest__name-value").get_text(strip=True)

    if team == "Tottenham": #Sunderland pro ověření
        print("..also the mood is 10 x")

if __name__ == "__main__":
    main()

    #strankaURL/robots.txt == prava a podminky na scraping
