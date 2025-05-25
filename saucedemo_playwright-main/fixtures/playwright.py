# ===================================== #
# Fixtures
# Ref: https://playwright.dev/python/docs/test-configuration
# Ref: https://playwright.dev/python/docs/test-runners
# Ref: https://playwright.dev/docs/test-fixtures (not written for python yet)
# ===================================== #
import time
import pytest


EXECUTION_TIME = time.strftime('%Y-%m-%d_%H-%M-%S')


@pytest.fixture(scope="session")
def browser_context_args(playwright):
    ## Ref: https://playwright.dev/python/docs/api/class-browsertype
    ## Ref: https://playwright.dev/python/docs/emulation
    # iphone_11 = playwright.devices["iPhone 11 Pro"]
    return {
        "is_mobile": False,
        "viewport": {
            "width": 1280, 
            "height": 720,
        },
        # **iphone_11,
        "accept_downloads": False,
        "ignore_https_errors": True,
        "locale": "en-US",
        "timezone_id":"Asia/Baku",
        "geolocation": {
            "longitude": 13.4050,
            "latitude": 52.5200
        },
        "permissions": ["geolocation"],
    }

@pytest.fixture
def page(browser, browser_context_args, request):
    context = browser.new_context(**browser_context_args)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path=f"traces/{EXECUTION_TIME}/trace-{request.node.name}.zip")
    context.close()