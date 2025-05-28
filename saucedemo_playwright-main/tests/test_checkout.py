import pytest
import json
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *
from pathlib import Path

#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1010 --browser=chromium --slowmo 500 --headed --html=report.html


#After the product is in the cart, the transition to the Checkout process.
@pytest.mark.tags("JIRA-1010", "ui", "checkout", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_checkout_page_should_be_opened_successfully(logged_in_page):
    page = logged_in_page
    page.locator(LOCATOR_TITLE).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_PRODUCTS_TITLE)
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_contain_text(CONSTANTS_CART_ADD_TO_CART_TEXT)
    page.locator(LOCATOR_ADD_TO_CART_BACKPACK).click()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_contain_text(CONSTANTS_CART_REMOVE_TEXT)
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_be_visible()
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_contain_text("1")
    page.locator(LOCATOR_SHOPPING_CART_LINK).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_contain_text("Checkout")
    page.locator(LOCATOR_CHECKOUT_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_YOUR_INFO_TITLE)
    expect(page.locator(LOCATOR_CHECKOUT_INFO)).to_be_visible()
   



#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1011 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1011", "ui", "checkout", "negative-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_checkout_page_should_not_be_opened_without_filling_fields(logged_in_page):
    page = logged_in_page
    page.locator(LOCATOR_TITLE).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_PRODUCTS_TITLE)
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_contain_text(CONSTANTS_CART_ADD_TO_CART_TEXT)
    page.locator(LOCATOR_ADD_TO_CART_BACKPACK).click()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_contain_text(CONSTANTS_CART_REMOVE_TEXT)
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_be_visible()
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_contain_text("1")
    page.locator(LOCATOR_SHOPPING_CART_LINK).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_contain_text("Checkout")
    page.locator(LOCATOR_CHECKOUT_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_YOUR_INFO_TITLE)
    expect(page.locator(LOCATOR_FIRST_NAME)).to_be_visible()
    expect(page.locator(LOCATOR_LAST_NAME)).to_be_visible()
    expect(page.locator(LOCATOR_POSTAL_CODE)).to_be_visible()
    page.locator(LOCATOR_CONTINUE_BUTTON).click()
    expect(page.locator(LOCATOR_ERROR)).to_be_visible()


#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1012 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1012", "ui", "checkout", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_checkout_page_should_be_opened_after_filling_fields(logged_in_page):
    page = logged_in_page
    page.locator(LOCATOR_TITLE).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_PRODUCTS_TITLE)
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_contain_text(CONSTANTS_CART_ADD_TO_CART_TEXT)
    page.locator(LOCATOR_ADD_TO_CART_BACKPACK).click()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_contain_text(CONSTANTS_CART_REMOVE_TEXT)
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_be_visible()
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_contain_text("1")
    page.locator(LOCATOR_SHOPPING_CART_LINK).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_contain_text("Checkout")
    page.locator(LOCATOR_CHECKOUT_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_YOUR_INFO_TITLE)
    expect(page.locator(LOCATOR_FIRST_NAME)).to_be_visible()
    expect(page.locator(LOCATOR_LAST_NAME)).to_be_visible()
    expect(page.locator(LOCATOR_POSTAL_CODE)).to_be_visible()
    page.locator(LOCATOR_FIRST_NAME).fill(CONSTANTS_CHECKOUT_FIRST_NAME)
    page.locator(LOCATOR_LAST_NAME).fill(CONSTANTS_CHECKOUT_LAST_NAME)
    page.locator(LOCATOR_POSTAL_CODE).fill(CONSTANTS_CHECKOUT_POSTAL_CODE)
    page.locator(LOCATOR_CONTINUE_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_OVERVIEW_TITLE)
    expect(page.locator(LOCATOR_SUMMARY_INFO)).to_be_visible()
    page.locator(LOCATOR_FINISH_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_COMPLETE_TITLE)
    expect(page.locator(LOCATOR_COMPLETE_HEADER)).to_be_visible()
    expect(page.locator(LOCATOR_COMPLETE_HEADER)).to_contain_text(CONSTANTS_CHECKOUT_THANK_YOU)


#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1013 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1013", "ui", "checkout", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_thank_you_for_your_order_should_be_seen_after_filling_fields_and_finish_order(logged_in_page):
    page = logged_in_page
    page.locator(LOCATOR_TITLE).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_PRODUCTS_TITLE)
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_contain_text(CONSTANTS_CART_ADD_TO_CART_TEXT)
    page.locator(LOCATOR_ADD_TO_CART_BACKPACK).click()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_contain_text(CONSTANTS_CART_REMOVE_TEXT)
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_be_visible()
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_contain_text("1")
    page.locator(LOCATOR_SHOPPING_CART_LINK).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_contain_text("Checkout")
    page.locator(LOCATOR_CHECKOUT_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_YOUR_INFO_TITLE)
    expect(page.locator(LOCATOR_FIRST_NAME)).to_be_visible()
    expect(page.locator(LOCATOR_LAST_NAME)).to_be_visible()
    expect(page.locator(LOCATOR_POSTAL_CODE)).to_be_visible()
    page.locator(LOCATOR_FIRST_NAME).fill(CONSTANTS_CHECKOUT_FIRST_NAME)
    page.locator(LOCATOR_LAST_NAME).fill(CONSTANTS_CHECKOUT_LAST_NAME)
    page.locator(LOCATOR_POSTAL_CODE).fill(CONSTANTS_CHECKOUT_POSTAL_CODE)
    page.locator(LOCATOR_CONTINUE_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_OVERVIEW_TITLE)
    expect(page.locator(LOCATOR_SUMMARY_INFO)).to_be_visible()
    page.locator(LOCATOR_FINISH_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_COMPLETE_TITLE)
    expect(page.locator(LOCATOR_COMPLETE_HEADER)).to_be_visible()
    expect(page.locator(LOCATOR_COMPLETE_HEADER)).to_contain_text(CONSTANTS_CHECKOUT_THANK_YOU)


#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1014 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1014", "ui", "checkout", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_total_price_should_be_equal_to_the_sum_of_prices_of_products_in_cart(logged_in_page):
    page = logged_in_page
    page.locator(LOCATOR_TITLE).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_PRODUCTS_TITLE)
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_contain_text(CONSTANTS_CART_ADD_TO_CART_TEXT)
    page.locator(LOCATOR_ADD_TO_CART_BACKPACK).click()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_contain_text(CONSTANTS_CART_REMOVE_TEXT)
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_be_visible()
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_contain_text("1")
    page.locator(LOCATOR_SHOPPING_CART_LINK).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_be_visible()
    expect(page.locator(LOCATOR_CHECKOUT_BUTTON)).to_contain_text("Checkout")
    page.locator(LOCATOR_CHECKOUT_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CHECKOUT_YOUR_INFO_TITLE)
    expect(page.locator(LOCATOR_FIRST_NAME)).to_be_visible()
    expect(page.locator(LOCATOR_LAST_NAME)).to_be_visible()
    expect(page.locator(LOCATOR_POSTAL_CODE)).to_be_visible()
    page.locator(LOCATOR_FIRST_NAME).fill(CONSTANTS_CHECKOUT_FIRST_NAME)
    page.locator(LOCATOR_LAST_NAME).fill(CONSTANTS_CHECKOUT_LAST_NAME)
    page.locator(LOCATOR_POSTAL_CODE).fill(CONSTANTS_CHECKOUT_POSTAL_CODE)
    page.locator(LOCATOR_CONTINUE_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    
    total_price_text = page.locator(LOCATOR_SUMMARY_TOTAL_LABEL).inner_text()
    total_price = float(total_price_text.replace('Total: $', '').replace(',', ''))
    PRODUCTS_JSON_PATH = Path(__file__).parent.parent.parent / "products.json"  
    with open(PRODUCTS_JSON_PATH, encoding="utf-8") as f:
        products_data = json.load(f)
    product_price = float(products_data[0]["price"].replace('$', '').replace(',', ''))
    tax_rate = 0.08
    expected_total_price = round(product_price + (product_price * tax_rate), 2)
    assert total_price == expected_total_price, f"Expected total price to be {expected_total_price}, but got {total_price}"
