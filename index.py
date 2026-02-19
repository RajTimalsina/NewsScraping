import requests 
from bs4 import BeautifulSoup
import time
import json
url=[
    "https://en.nepalkhabar.com/category/politics/",
    "https://english.ratopati.com/",
    "https://kathmandupost.com/politics"
]


allnews_list=[]
def get_news(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        response =requests.get(url,headers=headers,timeout=10)
        if response.status_code == 200:
            print("Successfully accessed the website")
        else:
            print(f"Failed to access the website. Status code: {response.status_code}")
            return []
        soup=BeautifulSoup(response.text,'html.parser')
        news_items=soup.find_all(['h3','h3.post-card_title'])
        print(f"Found {len(news_items)} news items\n")
        news_list=[]
        for item in news_items:
            title=item.get_text(strip=True)
            news_list.append(title)
            allnews_list.append(title)
            print(f"  {title}\n")



        with open('news.json', 'w', encoding='utf-8') as f:
            json.dump(allnews_list, f, ensure_ascii=False, indent=2)
    
        print(f"\n Saved {len(allnews_list)} news to news.json")
    
        time.sleep(2)
    except requests.Timeout:
        print("The request timed out")
    except Exception as e:
        print(f"An error occurred: {e}")



for link in url:
    print(f"Scraping news from: {link}")
    get_news(link)
    