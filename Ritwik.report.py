import requests
from bs4 import BeautifulSoup

def scrape_ndtv_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title_element = soup.find('h1', class_='story__title')
    summary_element = soup.find('div', class_='ins_storybody').p
    content_element = soup.find('div', class_='ins_storybody')
    
    # Check if elements exist before accessing their properties
    title = title_element.text.strip() if title_element else None
    summary = summary_element.text.strip() if summary_element else None
    content = '\n'.join([p.text.strip() for p in content_element.find_all('p')]) if content_element else None
    
    return {'title': title, 'summary': summary, 'content': content}

def scrape_times_now_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting the article title
    title = soup.find('h1').text.strip()
    
    # Extracting the article content
    content = '\n'.join([p.text.strip() for p in soup.find_all('p')])
    
    return {'title': title, 'content': content}

if _name_ == '_main_':
    # NDTV URL
    ndtv_url = 'https://www.ndtv.com/india-news/to-poison-voters-deve-gowda-grandson-prajwal-revanna-on-morphed-sex-videos-5540960#pfrom=home-ndtv_bigstory'
    ndtv_article_data = scrape_ndtv_article(ndtv_url)
    print("NDTV Article:")
    print("Title:", ndtv_article_data['title'])
    print("Summary:", ndtv_article_data['summary'])
    print("Content:", ndtv_article_data['content'])
    print()
    
    # Times Now URL
    times_now_url = 'https://www.timesnownews.com/india/article/arnab-goswami-afraid-of-yogi-adityanath-attacks-him-in-allahabad/835453'
    times_now_article_data = scrape_times_now_article(times_now_url)
    print("Times Now Article:")
    print("Title:", times_now_article_data['title'])
    print("Content:", times_now_article_data['content'])