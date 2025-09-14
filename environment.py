# environment.py
import yaml
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def before_all(context):
    # load config
    config_path = os.path.join(os.getcwd(), "config.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            context.cfg = yaml.safe_load(f)
    else:
        context.cfg = {}

    # Setup WebDriver for UI tests
    browser_config = context.cfg.get("browser", {})
    headless = browser_config.get("headless", True)

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
    context.driver.implicitly_wait(browser_config.get("implicit_wait", 5))


def after_all(context):
    try:
        if getattr(context, "driver", None):
            context.driver.quit()
    except Exception:
        pass
