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
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()
    expect(page.locator("[data-test=\"inventory-list\"] div").filter(has_text="Sauce Labs Backpackcarry.").nth(1)).to_be_visible()
    #save product title as variable 
    product_title = page.locator("[data-test=\"inventory-item-name\"]").nth(0).inner_text()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    expect(page.locator("[data-test=\"cart-list\"]")).to_be_visible()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")
    #save product in cart title as variable
    product_in_cart_title = page.locator("[data-test=\"inventory-item-name\"]").nth(0).inner_text()
    assert product_in_cart_title == product_title, f"Expected product in cart to be '{product_title}', but got '{product_in_cart_title}'"

# pytest saucedemo_playwright-main/tests/test_cart.py -v --tags JIRA-1008 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1008", "ui", "cart", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_multiple_products_should_be_added_to_the_cart_successfully(logged_in_page):
    page = logged_in_page
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()
    first_product_title = page.locator("[data-test=\"inventory-item-name\"]").nth(0).inner_text()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    second_product_title = page.locator("[data-test=\"inventory-item-name\"]").nth(1).inner_text()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("2")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    expect(page.locator("[data-test=\"cart-list\"]")).to_be_visible()
    cart_product_titles = page.locator("[data-test=\"inventory-item-name\"]")
    cart_titles = [cart_product_titles.nth(i).inner_text() for i in range(cart_product_titles.count())]
    assert first_product_title in cart_titles, f"First product '{first_product_title}' not found in cart. Cart contains: {cart_titles}"
    assert second_product_title in cart_titles, f"Second product '{second_product_title}' not found in cart. Cart contains: {cart_titles}"



# pytest saucedemo_playwright-main/tests/test_cart.py -v --tags JIRA-1009 --browser=chromium --slowmo 500 --headed --html=report.html

    #check the coreectly removing of products from the cart with remove button
@pytest.mark.tags("JIRA-1009", "ui", "cart", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_product_should_be_removed_from_the_cart_successfully(logged_in_page):
    page = logged_in_page
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()
    expect(page.locator("[data-test=\"inventory-list\"] div").filter(has_text="Sauce Labs Backpackcarry.").nth(1)).to_be_visible()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    expect(page.locator("[data-test=\"cart-list\"]")).to_be_visible()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")
    page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
    # After removing, check that the product is no longer in the cart
    expect(page.locator("[data-test=\"cart-list\"]")).to_be_visible()
    cart_titles = [el.inner_text() for el in page.locator("[data-test=\"inventory-item-name\"]").all()]
    assert "Sauce Labs Backpack" not in cart_titles, "Product 'Sauce Labs Backpack' was not removed from the cart successfully"