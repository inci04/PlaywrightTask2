import pytest
from data.constants import *
from data.locators import *


@pytest.fixture
def logged_in_page(page, request):
    user_type = request.param
    password = CONSTANTS_USERS.get(user_type)
    if not password:
        raise ValueError(f"No credentials found for user type '{user_type}'")

    page.goto(CONSTANTS_START_URL)
    page.locator(LOCATORS_AUTH_USERNAME).fill(user_type)
    page.locator(LOCATORS_AUTH_PASSWORD).fill(password)
    page.locator(LOCATORS_AUTH_LOGIN_BTN).click()
    return page