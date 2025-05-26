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
    page.locator("[data-test=\"title\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_contain_text("Checkout")
    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    expect(page.locator(".checkout_info")).to_be_visible()
   



#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1011 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1011", "ui", "checkout", "negative-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_checkout_page_should_not_be_opened_without_filling_fields(logged_in_page):
    page = logged_in_page
    page.locator("[data-test=\"title\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_contain_text("Checkout")
    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    expect(page.locator("#first-name")).to_be_visible()
    expect(page.locator("#last-name")).to_be_visible()
    expect(page.locator("#postal-code")).to_be_visible()
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()


#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1012 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1012", "ui", "checkout", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_checkout_page_should_be_opened_after_filling_fields(logged_in_page):
    page = logged_in_page
    page.locator("[data-test=\"title\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_contain_text("Checkout")
    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    expect(page.locator("#first-name")).to_be_visible()
    expect(page.locator("#last-name")).to_be_visible()
    expect(page.locator("#postal-code")).to_be_visible()
    page.locator("#first-name").fill("Inji")
    page.locator("#last-name").fill("Nuraliyeva")
    page.locator("#postal-code").fill("inji123")
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Overview")
    expect(page.locator(".summary_info")).to_be_visible()


#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1013 --browser=chromium --slowmo 500 --headed --html=report.html
#Thank you for your order! check if the message appears.
@pytest.mark.tags("JIRA-1013", "ui", "checkout", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_thank_you_for_your_order_should_be_seen_after_filling_fields_and_finish_order(logged_in_page):
    page = logged_in_page
    page.locator("[data-test=\"title\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_contain_text("Checkout")
    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    expect(page.locator("#first-name")).to_be_visible()
    expect(page.locator("#last-name")).to_be_visible()
    expect(page.locator("#postal-code")).to_be_visible()
    page.locator("#first-name").fill("Inji")
    page.locator("#last-name").fill("Nuraliyeva")
    page.locator("#postal-code").fill("inji123")
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Overview")
    expect(page.locator(".summary_info")).to_be_visible()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Complete!")
    expect(page.locator(".complete-header")).to_be_visible()
    expect(page.locator(".complete-header")).to_contain_text("Thank you for your order!")


#pytest saucedemo_playwright-main/tests/test_checkout.py -v --tags JIRA-1014 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1014", "ui", "checkout", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_total_price_should_be_equal_to_the_sum_of_prices_of_products_in_cart(logged_in_page):
    page = logged_in_page
    page.locator("[data-test=\"title\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout\"]")).to_contain_text("Checkout")
    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    expect(page.locator("#first-name")).to_be_visible()
    expect(page.locator("#last-name")).to_be_visible()
    expect(page.locator("#postal-code")).to_be_visible()
    page.locator("#first-name").fill("Inji")
    page.locator("#last-name").fill("Nuraliyeva")
    page.locator("#postal-code").fill("inji123")
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    
    total_price_text = page.locator(".summary_total_label").inner_text()
    total_price = float(total_price_text.replace('Total: $', '').replace(',', ''))
    PRODUCTS_JSON_PATH = Path(__file__).parent.parent.parent / "products.json"  
    with open(PRODUCTS_JSON_PATH, encoding="utf-8") as f:
        products_data = json.load(f)
    product_price = float(products_data[0]["price"].replace('$', '').replace(',', ''))
    tax_rate = 0.08
    expected_total_price = round(product_price + (product_price * tax_rate), 2)
    assert total_price == expected_total_price, f"Expected total price to be {expected_total_price}, but got {total_price}"
