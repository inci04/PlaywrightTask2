# ===================================== #
# Tests
# Ref: https://playwright.dev/python/docs/test-assertions
# ===================================== #
import pytest
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *


@pytest.mark.tags("JIRA-0001", "ui", "auth")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_standard_users_should_be_able_to_see_products(logged_in_page):
    # Auto waiting
    # -------------
    # Ref: https://playwright.dev/python/docs/actionability
    logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    logged_in_page.wait_for_timeout(2000) # Explicit wait for 2 seconds (delay)

    expect(logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(logged_in_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0002", "ui", "auth")
@pytest.mark.parametrize("logged_in_page", ["problem_user"], indirect=True)
def test_problem_users_should_be_able_to_see_products(logged_in_page):
    logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    expect(logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(logged_in_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0003", "ui", "auth")
@pytest.mark.parametrize("logged_in_page", ["locked_out_user"], indirect=True)
def test_locked_out_users_should_not_be_able_to_see_products(logged_in_page):
    expect(logged_in_page.locator(LOCATORS_AUTH_ERROR_MESSAGE)).to_have_text(CONSTANTS_AUTH_ERROR_MESSAGE)
    expect(logged_in_page).to_have_url(CONSTANTS_START_URL)


@pytest.mark.tags("JIRA-0004", "ui", "auth")
@pytest.mark.parametrize("logged_in_page", ["performance_glitch_user"], indirect=True)
def test_performance_glitch_users_should_be_able_to_see_products(logged_in_page):
    logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    expect(logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(logged_in_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0005", "ui", "auth")
@pytest.mark.parametrize("logged_in_page", ["error_user"], indirect=True)
def test_error_users_should_be_able_to_see_products(logged_in_page):
    logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    expect(logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(logged_in_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0006", "ui", "auth")
@pytest.mark.parametrize("logged_in_page", ["visual_user"], indirect=True)
def test_visual_users_should_be_able_to_see_products(logged_in_page):
    logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    expect(logged_in_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(logged_in_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")