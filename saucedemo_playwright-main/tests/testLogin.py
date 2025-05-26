import pytest
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *


@pytest.mark.tags("JIRA-1001", "ui", "auth", "standard_user", "positive_case")
def test_standard_users_should_be_able_to_login_successfully(page):
    page.goto(CONSTANTS_START_URL)
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    expect(page.locator("[data-test=\"password\"]")).to_be_visible()
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()


# pytest saucedemo_playwright-main/tests/testLogin.py -v --tags JIRA-1002 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1002", "ui", "auth", "standard_user", "negative_case")
def test_users_should_not_be_able_to_login_with_invalid_credentials(page):
    page.goto(CONSTANTS_START_URL)
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    expect(page.locator("[data-test=\"password\"]")).to_be_visible()
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("12345678")
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")


# pytest saucedemo_playwright-main/tests/testLogin.py -v --tags JIRA-1003 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1003", "ui", "auth", "locked_out_user", "negative_case")
def test_locked_out_user_should_not_able_to_login(page):
    page.goto(CONSTANTS_START_URL)
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    expect(page.locator("[data-test=\"password\"]")).to_be_visible()
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")


# pytest saucedemo_playwright-main/tests/testLogin.py -v --tags JIRA-1004 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-1004", "ui", "auth", "standard_user", "positive_case")
def test_standard_users_should_be_able_to_login_and_see_product_page(page):
    page.goto(CONSTANTS_START_URL)
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    expect(page.locator("[data-test=\"password\"]")).to_be_visible()
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")