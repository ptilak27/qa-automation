# environment.py
from selenium import webdriver
from utils.config import config
from utils.logger import logger
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def before_all(context):
    # Setup WebDriver for UI tests
    logger.info("Starting test execution")

    headless = config.browser_headless

    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Create driver only if UI tests are run (lazy create when needed)
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    context.driver.implicitly_wait(config.browser_implicit_wait)


def after_all(context):
    logger.info("Test execution completed")
    try:
        if getattr(context, "driver", None):
            context.driver.quit()
    except Exception:
        pass
