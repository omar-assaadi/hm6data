import requests
from datetime import datetime, timedelta

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    if not news_keywords or not all(keyword.isalpha() for keyword in news_keywords):
        raise ValueError("Invalid news keywords provided.")
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=lookback_days)
    
    query = ' AND '.join(news_keywords)
    url = f"https://newsapi.org/v2/everything?q={query}&from={start_date.strftime('%Y-%m-%d')}&to={end_date.strftime('%Y-%m-%d')}&language=en&apiKey={api_key}"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.status_code}")
    
    return response.json().get('articles', [])