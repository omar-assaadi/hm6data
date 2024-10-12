import json
import os
import argparse
from newscover.newsapi import fetch_latest_news

def main():
    parser = argparse.ArgumentParser(description="Collect news articles based on keywords.")
    parser.add_argument('-k', '--api_key', required=True, help='API key for News API')
    parser.add_argument('-b', '--lookback', type=int, default=10, help='Number of days to look back for news articles')
    parser.add_argument('-i', '--input_file', required=True, help='Input JSON file containing keyword lists')
    parser.add_argument('-o', '--output_dir', required=True, help='Directory to save output JSON files')

    args = parser.parse_args()

    # Load the keyword lists from the input file
    with open(args.input_file, 'r') as f:
        keyword_lists = json.load(f)

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Collect news articles for each keyword set
    for name, keywords in keyword_lists.items():
        articles = fetch_latest_news(args.api_key, keywords, args.lookback)
        output_file = os.path.join(args.output_dir, f"{name}.json")
        
        with open(output_file, 'w') as out_f:
            json.dump(articles, out_f, indent=4)

if __name__ == '__main__':
    main()
