import unittest
import json
import os
from newscover.newsapi import fetch_latest_news

def load_api_key():
    secrets_file_path = os.path.join(os.path.dirname(__file__), "test_secrets.json")
    with open(secrets_file_path, "r") as file:
        secrets = json.load(file)
        return secrets["api_key"]

class TestFetchLatestNews(unittest.TestCase):

    def setUp(self):
        self.api_key = load_api_key()

    def test_fetch_latest_news_no_keywords(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, news_keywords=[])

    def test_fetch_latest_news_within_lookback_days(self):
        articles = fetch_latest_news(self.api_key, news_keywords=["technology"], lookback_days=5)
        for article in articles:
            self.assertIn("publishedAt", article)
            published_date = article["publishedAt"]

    def test_fetch_latest_news_invalid_keywords(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, news_keywords=["news@20270"])  # Invalid keyword

if __name__ == "__main__":
    unittest.main()
