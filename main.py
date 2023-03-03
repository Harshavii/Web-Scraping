from bs4 import BeautifulSoup

#use encoding as utf-8, if there are any emojis or symbols in website
# here, website.html is used which was created manually for testing
with open("website.html",encoding='utf-8') as file:
    content = file.read()
    print(content)

# soup = BeautifulSoup(content, "html.parser")

print(soup.title)           
# returns "<title>your title of wp</title>"

print(soup.title.name)      
# returns only the title without tags

print(soup.title.string)    
# returns string of the title tag

# print(soup)
print(soup.prettify())
# used to represent soup data extracted from website in proper format

print(soup.a)             
# returns first anchor tag

all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)
# returns all anchor tags of ur specified webpage

# in order to get text of anchor tags
for tags in all_anchor_tags:
    # print(tags.getText())
    print(tags.get("href"))

h1= soup.findAll(name="h1", id="name")
print(h1)
# returns all data with h1 tags

# using class names
# use "class_" instead of "class"
section_heading = soup.find(name="h3", class_ = "heading")
# print(section_heading)
print(section_heading.get("class"))

# using css selectors
company_url = soup.select_one(selector="p a")
print(company_url)

# using id
# to get id use #
name = soup.select_one("#name")
print(name)

# to get all classes named heading use .heading
heading  = soup.select(selector=".heading")
print(heading)
