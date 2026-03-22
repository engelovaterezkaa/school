from playwright.sync_api import sync_playwright
import json

def main():
    with sync_playwright() as p:
        data = {}
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.kinoaero.cz/?sort=sort-by-data")

        movie_name = page.locator('div.program__movie-name').first.inner_text()

        price = page.locator('button.program__ticket.program__ticket--kino-aero').first.inner_text()
        # print(price)
        clean_price = price.replace("Kč", "").strip()

        page.goto("https://www.imdb.com/")

        page.fill('input.imdb-header-search__input.searchTypeahead__input.react-autosuggest__input', movie_name)

        page.click('button#suggestion-search-button')

        raw = page.locator('span.ipc-rating-star.ipc-rating-star--base.ipc-rating-star--imdb.ratingGroup--imdb-rating').first.inner_text()
        # print(rating)
        rating = raw.split() [0]
        rating_value = float(rating)

        print("Movie name:", movie_name)
        data["Movie name"] = movie_name

        print("Rating:", rating)
        data["Rating"] = rating

        result = int(clean_price)/rating_value

        print("Performance:", result)
        data["Performance"] = result

        browser.close()

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
