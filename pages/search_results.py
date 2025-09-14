# pages/search_results.py
from selenium.webdriver.common.by import By


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
