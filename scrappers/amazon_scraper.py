import requests
import pandas as pd
from bs4 import BeautifulSoup

class AmazonScraper:
    def scrape(self, query):
        url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")
        items = []

        for item in soup.select(".s-result-item"):
            try:
                title = item.select_one("h2 span").text
                price = item.select_one(".a-price-whole")
                rating = item.select_one(".a-icon-alt")
                reviews = item.select_one(".a-size-base")

                if not price:
                    continue

                items.append({
                    "title": title,
                    "price": int(price.text.replace(",", "")),
                    "rating": float(rating.text.split()[0]) if rating else None,
                    "reviews": int(reviews.text.replace(",", "")) if reviews else 0,
                    "source": "Amazon"
                })
            except:
                continue

        return pd.DataFrame(items)
