# pages/amazon_home.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonHome:
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)

    def search(self, search_string):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        search_box = self.driver.find_element(self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(search_string)
        self.driver.find_element(self.SEARCH_BUTTON).click()
