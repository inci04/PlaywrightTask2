import pytest
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *

# pytest saucedemo_playwright-main/tests/test_logout.py -v --tags JIRA-1015 --browser=chromium --slowmo 500 --headed --html=report.html
@pytest.mark.tags("JIRA-1015", "ui", "logout", "positive-case")
@pytest.mark.parametrize("logged_in_page", ["standard_user"], indirect=True)
def test_logout_functionality(logged_in_page):
    page = logged_in_page
    expect(page.locator(LOCATOR_TITLE)).to_be_visible()
    expect(page.locator(LOCATOR_TITLE)).to_contain_text(CONSTANTS_LOGOUT_PRODUCTS_TITLE)
    expect(page.get_by_role("button", name="Open Menu")).to_be_visible()
    page.get_by_role("button", name="Open Menu").click()
    expect(page.locator(LOCATOR_LOGOUT_SIDEBAR_LINK)).to_be_visible()
    expect(page.locator(LOCATOR_LOGOUT_SIDEBAR_LINK)).to_contain_text(CONSTANTS_LOGOUT_SIDEBAR_TEXT)
    page.locator(LOCATOR_LOGOUT_SIDEBAR_LINK).click()
    expect(page.locator(LOCATOR_LOGIN_CONTAINER).filter(has_text=CONSTANTS_LOGOUT_LOGIN_TEXT).first).to_be_visible()