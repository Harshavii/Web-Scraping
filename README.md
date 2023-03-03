day45_Web-Scraping

In this repository, web scraping is done using Beautiful Soup module.
Web pages are accessed using requests.

Used "html.parser" here.
For extracting xml data, use lxml parser.
So, here are two python files:
1. main.py
2. bs.py

In main.py, I have used webpage which I created earlier in my local system named website.html for testing.
While in bs.py, ycombinator news webpage data is extracted using BeautifulSoup. 
Basically, it gets the link and heading of the latest news available having most number of upvotes.

Alternatively, Selenium can also be used for web scraping.
It interacts with browsers with the help of drivers.
