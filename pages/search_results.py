# pages/search_results.py
from selenium.webdriver.common.by import By
from utils.logger import logger
from utils.config import config


class SearchResults:
    PRODUCT_CONTAINERS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 a span")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".a-price-whole")
    PRODUCT_PRICE_FRACTION = (By.CSS_SELECTOR, ".a-price-fraction")
    PRODUCT_RATING = (By.CSS_SELECTOR, ".a-icon-alt")
    PRODUCT_LINK = (By.CSS_SELECTOR, "h2 a")

    def __init__(self, driver):
        self.driver = driver
        self.products = []

    def get_product_details(self):
        """Extract product details from search results page"""
        try:
            logger.info("Extracting product details from search results")
            self.products = []

            product_containers = self.find_elements(
                self.PRODUCT_CONTAINERS, timeout=config.browser_implicit_wait
            )

            if not product_containers:
                logger.info("Primary selectors didn't work, trying alternatives")
                product_containers = self.find_elements(
                    self.ALT_PRODUCT_CONTAINERS, timeout=config.browser_implicit_wait
                )

            if not product_containers:
                logger.warning("No product containers found")
                return self.products

            logger.info(f"Found {len(product_containers)} product containers")

            for i, container in enumerate(
                product_containers[:10]
            ):  # Limit to first 10 products
                continue

            logger.info(
                f"Successfully extracted details for {len(self.products)} products"
            )
            return self.products

        except Exception as e:
            logger.error(f"Failed to get product details: {str(e)}")
            raise
