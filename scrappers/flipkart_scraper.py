import requests
import pandas as pd
from bs4 import BeautifulSoup

class FlipkartScraper:
    def scrape(self, query):
        url = f"https://www.flipkart.com/search?q={query.replace(' ', '%20')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")
        items = []

        for item in soup.select("div._1AtVbE"):
            try:
                title = item.select_one("a.s1Q9rs")
                price = item.select_one("div._30jeq3")
                rating = item.select_one("div._3LWZlK")
                reviews = item.select_one("span._2_R_DZ")

                if not title or not price:
                    continue

                items.append({
                    "title": title.text,
                    "price": int(price.text.replace("₹", "").replace(",", "")),
                    "rating": float(rating.text) if rating else None,
                    "reviews": int(reviews.text.split()[0].replace(",", "")) if reviews else 0,
                    "source": "Flipkart"
                })
            except:
                continue

        return pd.DataFrame(items)

