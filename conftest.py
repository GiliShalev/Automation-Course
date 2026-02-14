import pytest
from playwright.sync_api import Page, BrowserContext, Browser
@pytest.fixture(scope="class", autouse=True)
def session_page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    yield page
    context.close()


@pytest.fixture(scope="class")
def class_page(browser: Browser):
    """Class-scoped fixture that creates a Page from Browser and yields it."""
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    yield page
    context.close()