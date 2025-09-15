# pages/search_results.py
from selenium.webdriver.common.by import By
from utils.logger import logger


class SearchResults:
    PRODUCT_CONTAINERS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".a-price-whole")
    PRODUCT_PRICE_FRACTION = (By.CSS_SELECTOR, ".a-price-fraction")
    PRODUCT_RATING = (By.CSS_SELECTOR, "a.a-popover-trigger")

    def __init__(self, driver):
        self.driver = driver
        self.products = []

    def get_product_details(self):
        """Extract product details from search results page"""
        try:
            logger.info("Extracting product details from search results")
            self.products = []

            product_containers = self.driver.find_elements(*self.PRODUCT_CONTAINERS)

            if not product_containers:
                logger.warning("No product containers found")
                return self.products

            logger.info(f"Found {len(product_containers)} product containers")

            # Extract details from each product container
            for i, container in enumerate(
                product_containers[:10]
            ):  # Limit to first 10 products
                try:
                    product_info = self._extract_single_product_info(container, i + 1)
                    if product_info:
                        self.products.append(product_info)
                        logger.info(f"Product {i+1}: {product_info}")

                except Exception as e:
                    logger.warning(
                        f"Failed to extract info for product {i+1}: {str(e)}"
                    )
                    continue

            logger.info(
                f"Successfully extracted details for {len(self.products)} products"
            )
            return self.products

        except Exception as e:
            logger.error(f"Failed to get product details: {str(e)}")
            raise

    def _extract_single_product_info(self, container, product_number):
        """Extract information from a single product container"""
        product_info = {
            "product_number": product_number,
            "title": "N/A",
            "price": "N/A",
            "rating": "N/A",
        }

        try:
            # Extract title
            title_elements = container.find_elements(*self.PRODUCT_TITLE)
            if title_elements:
                product_info["title"] = title_elements[0].text.strip()

            # Extract price
            price_whole_elements = container.find_elements(*self.PRODUCT_PRICE)
            price_fraction_elements = container.find_elements(
                *self.PRODUCT_PRICE_FRACTION
            )

            if price_whole_elements:
                price_whole = price_whole_elements[0].text.strip()
                price_fraction = ""
                if price_fraction_elements:
                    price_fraction = price_fraction_elements[0].text.strip()
                product_info["price"] = (
                    f"₹{price_whole}.{price_fraction}"
                    if price_fraction
                    else f"₹{price_whole}"
                )

            # Extract rating
            rating_elements = container.find_elements(*self.PRODUCT_RATING)
            if rating_elements:
                rating_text = (
                    rating_elements[0].get_attribute("aria-label")
                    or rating_elements[0].text
                )
                if rating_text and "out of" in rating_text.lower():
                    # Extract numeric rating from text like "4.2 out of 5 stars"
                    rating_parts = rating_text.split()
                    if rating_parts:
                        product_info["rating"] = rating_parts[0]
                else:
                    product_info["rating"] = rating_text

        except Exception as e:
            logger.warning(
                f"Error extracting details for product {product_number}: {str(e)}"
            )

        return product_info

    def print_product_details(self):
        """Print all extracted product details"""
        if not self.products:
            logger.warning("No products to display")
            return

        logger.info("\n" + "=" * 80)
        logger.info("AMAZON SEARCH RESULTS - PRODUCT DETAILS")
        logger.info("=" * 80)

        for product in self.products:
            logger.info(f"\nProduct {product['product_number']}:")
            logger.info(f"  Title: {product['title']}")
            logger.info(f"  Price: {product['price']}")
            logger.info(f"  Rating: {product['rating']}")
            logger.info("-" * 40)

        logger.info(f"\nTotal products extracted: {len(self.products)}")
        logger.info("=" * 80)

    def get_products_list(self):
        """Return the list of extracted products"""
        return self.products
