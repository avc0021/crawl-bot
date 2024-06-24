from scraper.scraper import fetch_titles

def main():
    url = 'https://www.scrapethissite.com/pages/'
    titles = fetch_titles(url)
    for title in titles:
        print(title)

if __name__ == "__main__":
    main()
