# pages/amazon_home.py
from selenium.webdriver.common.by import By
from utils.logger import logger
from utils.config import config
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonHome:
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)

    def search(self, search_string):
        try:
            logger.info(f"Searching for: {search_string}")

            # Clear and enter search term
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SEARCH_BOX)
            )
            search_box = self.driver.find_element(self.SEARCH_BOX)
            search_box.clear()
            search_box.send_keys(search_string)
            search_box.send_keys(Keys.ENTER)

            # Wait for search results to load
            time.sleep(config.browser_implicit_wait)
            logger.info("Search completed successfully")

        except Exception as e:
            logger.error(f"Failed to search for {search_string}: {str(e)}")
            raise
