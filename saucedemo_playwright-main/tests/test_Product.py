# Saytda göstərilən məhsul adlarının və qiymətlərinin düzgün göstərildiyini yoxlayın.
# pytest tests/products_list/test_products.py -v --tags products-data-in-UI --browser=chromium --slowmo 500 --headed --html=report.html
# Ensure LOCATORS_ITEM_NAMES is imported from data/locators.py
import json
import pytest
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *
from pathlib import Path

 # pytest saucedemo_playwright-main/tests/test_Product.py -v --tags JIRA-1005 --browser=chromium --slowmo 500 --headed --html=report.html

PRODUCTS_JSON_PATH = Path(__file__).parent.parent.parent / "products.json"
with open(PRODUCTS_JSON_PATH, encoding="utf-8") as f:
    products_data = json.load(f)

@pytest.mark.tags("JIRA-1005", "ui", "products-list", "products-data-in-UI", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_products_list_all_product_data_from_API_is_visible_on_UI(logged_in_page):
    # Check that the inventory list container is visible
    expect(logged_in_page.locator('[data-test="inventory-list"]')).to_be_visible()
    # Check that the products page title is correct
    expect(logged_in_page.locator('span[data-test="title"]')).to_contain_text('Products')
    # Get all product name and price elements from the UI
    ui_product_names = logged_in_page.locator('[data-test="inventory-item-name"]')
    ui_product_prices = logged_in_page.locator('[data-test="inventory-item-price"]')
    # Extract text from UI elements
    ui_names = [ui_product_names.nth(i).inner_text().strip() for i in range(ui_product_names.count())]
    ui_prices = [ui_product_prices.nth(i).inner_text().strip() for i in range(ui_product_prices.count())]
    # Extract expected names and prices from JSON
    expected_names = [product["name"] for product in products_data]
    expected_prices = [product["price"] for product in products_data]
    # Check that all expected names and prices are present in the UI
    for name, price in zip(expected_names, expected_prices):
        assert name in ui_names, f"Product name '{name}' not found on UI"
        assert price in ui_prices, f"Product price '{price}' not found on UI"



 # pytest saucedemo_playwright-main/tests/test_Product.py -v --tags JIRA-1006 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1006", "ui", "products-list", "products-data-in-UI", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_products_prices_from_high_to_low(logged_in_page):
    # Check that the inventory list container is visible
    expect(logged_in_page.locator('[data-test="inventory-list"]')).to_be_visible()
    # Check that the products page title is correct
    expect(logged_in_page.locator('span[data-test="title"]')).to_contain_text('Products')
    # Get all product price elements from the UI
    ui_product_prices = logged_in_page.locator('[data-test="inventory-item-price"]')
    # Extract text from UI elements
    ui_prices = [ui_product_prices.nth(i).inner_text().strip() for i in range(ui_product_prices.count())]
    # Convert prices to float for comparison
    ui_prices_float = [float(price.replace('$', '')) for price in ui_prices]
    # Get expected prices from JSON and convert to float
    expected_prices = [product["price"] for product in products_data]
    expected_prices_float = [float(price.replace('$', '')) for price in expected_prices]
    # Sort both lists in descending order
    ui_prices_float.sort(reverse=True)
    expected_prices_float.sort(reverse=True)
    # Check that the sorted lists are equal
    assert ui_prices_float == expected_prices_float, "Product prices are not sorted correctly from high to low"
