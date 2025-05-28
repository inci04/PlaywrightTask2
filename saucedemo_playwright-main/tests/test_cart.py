import pytest
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *

 # pytest saucedemo_playwright-main/tests/test_cart.py -v --tags JIRA-1007 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1007", "ui", "cart", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_product_should_be_added_to_the_cart_successfully(logged_in_page):
    page = logged_in_page
    expect(page.locator(LOCATOR_INVENTORY_CONTAINER)).to_be_visible()
    expect(page.locator(LOCATOR_INVENTORY_LIST + ' div').filter(has_text=CONSTANTS_CART_PRODUCT_1 + 'carry.').nth(1)).to_be_visible()
    #save product title as variable 
    product_title = page.locator(LOCATOR_INVENTORY_ITEM_NAME).nth(0).inner_text()
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_be_visible()
    expect(page.locator(LOCATOR_ADD_TO_CART_BACKPACK)).to_contain_text(CONSTANTS_CART_ADD_TO_CART_TEXT)
    page.locator(LOCATOR_ADD_TO_CART_BACKPACK).click()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_contain_text(CONSTANTS_CART_REMOVE_TEXT)
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_contain_text("1")
    page.locator(LOCATOR_SHOPPING_CART_LINK).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CART_TITLE)
    expect(page.locator(LOCATOR_CART_LIST)).to_be_visible()
    expect(page.locator(LOCATOR_INVENTORY_ITEM_NAME)).to_contain_text(CONSTANTS_CART_PRODUCT_1)
    #save product in cart title as variable
    product_in_cart_title = page.locator(LOCATOR_INVENTORY_ITEM_NAME).nth(0).inner_text()
    assert product_in_cart_title == product_title, f"Expected product in cart to be '{product_title}', but got '{product_in_cart_title}'"

# pytest saucedemo_playwright-main/tests/test_cart.py -v --tags JIRA-1008 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1008", "ui", "cart", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_multiple_products_should_be_added_to_the_cart_successfully(logged_in_page):
    page = logged_in_page
    expect(page.locator(LOCATOR_INVENTORY_CONTAINER)).to_be_visible()
    first_product_title = page.locator(LOCATOR_INVENTORY_ITEM_NAME).nth(0).inner_text()
    page.locator(LOCATOR_ADD_TO_CART_BACKPACK).click()
    second_product_title = page.locator(LOCATOR_INVENTORY_ITEM_NAME).nth(1).inner_text()
    page.locator(LOCATOR_ADD_TO_CART_BIKE_LIGHT).click()
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_contain_text("2")
    page.locator(LOCATOR_SHOPPING_CART_LINK).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CART_TITLE)
    expect(page.locator(LOCATOR_CART_LIST)).to_be_visible()
    cart_product_titles = page.locator(LOCATOR_INVENTORY_ITEM_NAME)
    cart_titles = [cart_product_titles.nth(i).inner_text() for i in range(cart_product_titles.count())]
    assert first_product_title in cart_titles, f"First product '{first_product_title}' not found in cart. Cart contains: {cart_titles}"
    assert second_product_title in cart_titles, f"Second product '{second_product_title}' not found in cart. Cart contains: {cart_titles}"



# pytest saucedemo_playwright-main/tests/test_cart.py -v --tags JIRA-1009 --browser=chromium --slowmo 500 --headed --html=report.html

    #check the coreectly removing of products from the cart with remove button
@pytest.mark.tags("JIRA-1009", "ui", "cart", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_product_should_be_removed_from_the_cart_successfully(logged_in_page):
    page = logged_in_page
    expect(page.locator(LOCATOR_INVENTORY_CONTAINER)).to_be_visible()
    expect(page.locator(LOCATOR_INVENTORY_LIST + ' div').filter(has_text=CONSTANTS_CART_PRODUCT_1 + 'carry.').nth(1)).to_be_visible()
    page.locator(LOCATOR_ADD_TO_CART_BACKPACK).click()
    expect(page.locator(LOCATOR_REMOVE_BACKPACK)).to_contain_text(CONSTANTS_CART_REMOVE_TEXT)
    expect(page.locator(LOCATOR_SHOPPING_CART_LINK)).to_contain_text("1")
    page.locator(LOCATOR_SHOPPING_CART_LINK).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_CART_TITLE)
    expect(page.locator(LOCATOR_CART_LIST)).to_be_visible()
    expect(page.locator(LOCATOR_INVENTORY_ITEM_NAME)).to_contain_text(CONSTANTS_CART_PRODUCT_1)
    page.locator(LOCATOR_REMOVE_BACKPACK).click()
    # After removing, check that the product is no longer in the cart
    expect(page.locator(LOCATOR_CART_LIST)).to_be_visible()
    cart_titles = [el.inner_text() for el in page.locator(LOCATOR_INVENTORY_ITEM_NAME).all()]
    assert CONSTANTS_CART_PRODUCT_1 not in cart_titles, f"Product '{CONSTANTS_CART_PRODUCT_1}' was not removed from the cart successfully"