from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

article = soup.find_all(name="a", class_="storylink")

article_text = []
article_links = []

for article in article:
    article_text.append(article.getText())
    article_links.append(article.get("href"))

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

article_index = article_scores.index(max(article_scores))

print(article_text[article_index])
print(article_links[article_index])