from behave import given, when, then
from pages.amazon_home import AmazonHome
from pages.search_results import SearchResults
from utils.config import config
from utils.logger import logger
import allure
import time


@given("I navigate to Amazon India website")
def step_navigate_to_amazon(context):
    """Navigate to Amazon India website"""
    try:
        context.amazon_home = AmazonHome(context.driver, config.amazon_url)
        context.search_results = SearchResults(context.driver)
        context.amazon_home.open()
        time.sleep(3)  # Wait for page to load

        logger.info("Successfully navigated to Amazon India")

    except Exception as e:
        logger.error(f"Failed to navigate to Amazon: {str(e)}")
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="navigation_failed",
            attachment_type=allure.attachment_type.PNG,
        )
        raise


@when('I search for "{search_string}"')
def step_search_for_product(context, search_string):
    """Search for a product on Amazon"""
    try:
        context.amazon_home.search(search_string)
        context.search_string = search_string
        time.sleep(config.browser_implicit_wait)  # Wait for search results

        logger.info(f"Successfully searched for: {search_string}")

    except Exception as e:
        logger.error(f"Failed to search for {search_string}: {str(e)}")
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="search_failed",
            attachment_type=allure.attachment_type.PNG,
        )
        raise


@then("I should see search results")
def step_verify_search_results(context):
    """Verify search results are displayed"""
    try:
        # Wait a bit more for results to load
        time.sleep(2)

        # Check if we can find product containers
        product_containers = context.driver.find_elements(
            *context.search_results.PRODUCT_CONTAINERS
        )

        assert len(product_containers) > 0, "No search results found"

        logger.info(f"Found {len(product_containers)} search results")

        # Take screenshot of search results
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="search_results",
            attachment_type=allure.attachment_type.PNG,
        )

    except Exception as e:
        logger.error(f"Search results verification failed: {str(e)}")
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="search_results_failed",
            attachment_type=allure.attachment_type.PNG,
        )
        raise


@then("I extract product details from page 1")
def step_extract_product_details(context):
    """Extract product details from search results"""
    try:
        products = context.search_results.get_product_details()
        context.products = products

        assert len(products) > 0, "No product details extracted"

        logger.info(f"Successfully extracted details for {len(products)} products")

        # Attach product details to allure report
        product_summary = f"Extracted {len(products)} products:\n"
        for product in products[:5]:  # Show first 5 products in summary
            product_summary += f"- {product['title'][:50]}... | Price: {product['price']} | Rating: {product['rating']}\n"

        allure.attach(
            product_summary,
            name="extracted_products",
            attachment_type=allure.attachment_type.TEXT,
        )

    except Exception as e:
        logger.error(f"Failed to extract product details: {str(e)}")
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="extraction_failed",
            attachment_type=allure.attachment_type.PNG,
        )
        raise


@then("I print the product information")
def step_print_product_information(context):
    """Print extracted product information"""
    try:
        context.search_results.print_product_details()

        # Also print to console for immediate visibility
        print("\n" + "=" * 80)
        print("AMAZON MOBILE SEARCH RESULTS")
        print("=" * 80)

        for product in context.products:
            print(f"\nProduct {product['product_number']}:")
            print(f"  📱 Title: {product['title']}")
            print(f"  💰 Price: {product['price']}")
            print(f"  ⭐ Rating: {product['rating']}")
            print("-" * 40)

        print(f"\n✅ Total products extracted: {len(context.products)}")
        print("=" * 80)

        logger.info("Product information printed successfully")

    except Exception as e:
        logger.error(f"Failed to print product information: {str(e)}")
        raise
