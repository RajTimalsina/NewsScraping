#  Nepal Politics News Scraper

A simple Python web scraper that collects the latest political news headlines from popular Nepali news websites and stores them in a JSON file.

---

##  Description

This project scrapes political news headlines from:

- https://en.nepalkhabar.com/category/politics/
- https://english.ratopati.com/
- https://kathmandupost.com/politics

The script sends HTTP requests to each website, extracts headline elements using BeautifulSoup, and saves all collected titles into a `news.json` file.

---

##  Features

- Scrapes multiple news websites
- Uses custom headers to reduce blocking
- Extracts headlines automatically
- Saves results in JSON format
- Handles request timeout errors
- Adds delay between requests to avoid overwhelming servers

---

##  Technologies Used

- Python 3
- requests
- BeautifulSoup (bs4)
- json
- time

---



