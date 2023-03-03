from bs4 import BeautifulSoup

#use encoding as utf-8 if there are any emojis or symbols in website
with open("website.html",encoding='utf-8') as file:
    content = file.read()
    # print(content)

# soup = BeautifulSoup(content, "html.parser")

# print(soup.title)           returns<title>Angela's Personal Site</title>
# print(soup.title.name)      returns title
# print(soup.title.string)    returns Angela's Personal Site

# print(soup)
# print(soup.prettify())
# print(soup.a)             returns first anchor tag

# all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)
#
# # in order to get text of anchor tags
# for tags in all_anchor_tags:
#     # print(tags.getText())
#     print(tags.get("href"))

# h1= soup.findAll(name="h1", id="name")
# print(h1)
#
# # use class_ instead of class
# section_heading = soup.find(name="h3", class_ = "heading")
# # print(section_heading)
# print(section_heading.get("class"))

# using css selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# # to get id use #
# name = soup.select_one("#name")
# print(name)

# to get all classes named heading use .heading
# heading  = soup.select(selector=".heading")
# print(heading)


import requests

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



