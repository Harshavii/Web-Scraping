import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
titles = []
links = []
upvotes = []

articles = soup.find_all(class_="titleline")
# print(articles)
for info in articles:
    article_title = info.find(name="a").getText()
    titles.append(article_title)
    article_link = info.find(name="a").get("href")
    links.append(article_link)
# print(titles)
# print(links)

article_upvote = soup.find_all(name="span", class_="score")
# for votes in article_upvote:
#     upvotes.append(votes.getText())
# print(upvotes)

upvotes = [int(votes.getText().split(" ")[0]) for votes in article_upvote]
# print(upvotes)

ln = max(upvotes)
# print(ln)

index = upvotes.index(ln)
# print(index)
print("Most popular news with highest upvote is:")
print(titles[index])
print(f"With {upvotes[index]} upvotes!")
print("And here's the link:")
print(links[index])



