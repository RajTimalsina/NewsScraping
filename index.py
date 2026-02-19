import requests 
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime
from urllib.parse import urlparse

url=[
    "https://english.ratopati.com/",
    "https://kathmandupost.com/politics"
]

def get_news(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print("Successfully accessed the website")
        else:
            print(f"Failed to access the website. Status code: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all(['h3', 'h2'])
        print(f"Found {len(news_items)} news items\n")
        
        news_list = []
        for item in news_items:
            title = item.get_text(strip=True)
            news_list.append({
                "title": title,
                "timestamp": datetime.now().isoformat()
            })
            print(f"  {title}\n")
        
        time.sleep(2)
        return news_list
        
    except requests.Timeout:
        print("The request timed out")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


today = datetime.now().strftime("%Y-%m-%d")

try:
    with open('news.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    # If old format (list), convert to new format (dict)
    if isinstance(data, list):
        data = {}
except:
    data = {}

if today not in data:
    data[today] = {}


for link in url:
    print(f"Scraping news from: {link}")
    website = urlparse(link).netloc
    news = get_news(link)
    
    if website not in data[today]:
        data[today][website] = []
    
    data[today][website].extend(news)


with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("News saved to news.json")
    