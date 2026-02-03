from amazon_scraper import AmazonScraper
from flipkart_scraper import FlipkartScraper

def run_all(query):
    amazon = AmazonScraper().scrape(query)
    flipkart = FlipkartScraper().scrape(query)

    amazon.to_excel("data/amazon.xlsx", index=False)
    flipkart.to_excel("data/flipkart.xlsx", index=False)

    print("✅ Scraping completed and Excel files saved")
