import pytest
from selene import browser


@pytest.fixture
def open_duckduckgo(setting_browser):
    browser.open('https://duckduckgo.com')
    yield
    browser.quit()


@pytest.fixture
def setting_browser():
    browser.config.window_width = 1200
    browser.config.window_height = 700
