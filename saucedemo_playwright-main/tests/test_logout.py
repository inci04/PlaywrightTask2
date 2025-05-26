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
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"primary-header\"] div").filter(has_text="Swag Labs").first).to_be_visible()
    page.get_by_role("button", name="Open Menu").click()
    expect(page.locator("[data-test=\"logout-sidebar-link\"]")).to_be_visible()
    expect(page.locator("[data-test=\"logout-sidebar-link\"]")).to_contain_text("Logout")
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("[data-test=\"login-container\"] div").filter(has_text="Login").first).to_be_visible()
    