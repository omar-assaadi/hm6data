from newsapi import fetch_latest_news

def main():
    api_key = "42d3df2d018e46989d093d8b97969310"  # Replace with your actual API key
    news_keywords = ["trump", "trial"]  # Example keywords
    lookback_days = 10  # Example number of days to look back

    # Call the function and print the results
    try:
        articles = fetch_latest_news(api_key, news_keywords, lookback_days)
        print(f"Found {len(articles)} articles:")
        for article in articles:
            print(article["title"])  # Print the title of each article
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
