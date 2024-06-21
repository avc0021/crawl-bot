import requests
from bs4 import BeautifulSoup

def fetch_titles(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('h2', class_='article-title')
        titles = [article.get_text() for article in articles]
        return titles
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []
