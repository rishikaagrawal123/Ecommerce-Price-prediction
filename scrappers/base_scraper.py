class BaseScraper:
    def scrape(self, query: str):
        """
        Must return pandas DataFrame with:
        title, price, rating, reviews, source
        """
        raise NotImplementedError
