import pytest
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *


@pytest.mark.tags("JIRA-1001", "ui", "auth", "standard_user", "positive_case")
def test_standard_users_should_be_able_to_login_successfully(page):
    page.goto(CONSTANTS_START_URL)
    expect(page.locator(LOCATOR_LOGIN_USERNAME)).to_be_visible()
    page.locator(LOCATOR_LOGIN_USERNAME).click()
    page.locator(LOCATOR_LOGIN_USERNAME).fill(CONSTANTS_LOGIN_USERNAME)
    expect(page.locator(LOCATOR_LOGIN_PASSWORD)).to_be_visible()
    page.locator(LOCATOR_LOGIN_PASSWORD).click()
    page.locator(LOCATOR_LOGIN_PASSWORD).fill(CONSTANTS_LOGIN_PASSWORD)
    expect(page.locator(LOCATOR_LOGIN_BUTTON)).to_be_visible()
    page.locator(LOCATOR_LOGIN_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()


# pytest saucedemo_playwright-main/tests/testLogin.py -v --tags JIRA-1002 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1002", "ui", "auth", "standard_user", "negative_case")
def test_users_should_not_be_able_to_login_with_invalid_credentials(page):
    page.goto(CONSTANTS_START_URL)
    expect(page.locator(LOCATOR_LOGIN_USERNAME)).to_be_visible()
    page.locator(LOCATOR_LOGIN_USERNAME).click()
    page.locator(LOCATOR_LOGIN_USERNAME).fill(CONSTANTS_LOGIN_USERNAME)
    expect(page.locator(LOCATOR_LOGIN_PASSWORD)).to_be_visible()
    page.locator(LOCATOR_LOGIN_PASSWORD).click()
    page.locator(LOCATOR_LOGIN_PASSWORD).fill(CONSTANTS_INVALID_PASSWORD)
    expect(page.locator(LOCATOR_LOGIN_BUTTON)).to_be_visible()
    page.locator(LOCATOR_LOGIN_BUTTON).click()
    expect(page.locator(LOCATOR_LOGIN_ERROR)).to_be_visible()
    expect(page.locator(LOCATOR_LOGIN_ERROR)).to_contain_text(CONSTANTS_LOGIN_ERROR_INVALID)


# pytest saucedemo_playwright-main/tests/testLogin.py -v --tags JIRA-1003 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1003", "ui", "auth", "locked_out_user", "negative_case")
def test_locked_out_user_should_not_able_to_login(page):
    page.goto(CONSTANTS_START_URL)
    expect(page.locator(LOCATOR_LOGIN_USERNAME)).to_be_visible()
    page.locator(LOCATOR_LOGIN_USERNAME).click()
    page.locator(LOCATOR_LOGIN_USERNAME).fill(CONSTANTS_LOCKED_OUT_USER)
    expect(page.locator(LOCATOR_LOGIN_PASSWORD)).to_be_visible()
    page.locator(LOCATOR_LOGIN_PASSWORD).click()
    page.locator(LOCATOR_LOGIN_PASSWORD).fill(CONSTANTS_LOGIN_PASSWORD)
    expect(page.locator(LOCATOR_LOGIN_BUTTON)).to_be_visible()
    page.locator(LOCATOR_LOGIN_BUTTON).click()
    expect(page.locator(LOCATOR_LOGIN_ERROR)).to_be_visible()
    expect(page.locator(LOCATOR_LOGIN_ERROR)).to_contain_text(CONSTANTS_LOGIN_ERROR_LOCKED_OUT)


# pytest saucedemo_playwright-main/tests/testLogin.py -v --tags JIRA-1004 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1004", "ui", "auth", "standard_user", "positive_case")
def test_standard_users_should_be_able_to_login_and_see_product_page(page):
    page.goto(CONSTANTS_START_URL)
    expect(page.locator(LOCATOR_LOGIN_USERNAME)).to_be_visible()
    page.locator(LOCATOR_LOGIN_USERNAME).click()
    page.locator(LOCATOR_LOGIN_USERNAME).fill(CONSTANTS_LOGIN_USERNAME)
    expect(page.locator(LOCATOR_LOGIN_PASSWORD)).to_be_visible()
    page.locator(LOCATOR_LOGIN_PASSWORD).click()
    page.locator(LOCATOR_LOGIN_PASSWORD).fill(CONSTANTS_LOGIN_PASSWORD)
    expect(page.locator(LOCATOR_LOGIN_BUTTON)).to_be_visible()
    page.locator(LOCATOR_LOGIN_BUTTON).click()
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_PRODUCTS_PAGE_TITLE)