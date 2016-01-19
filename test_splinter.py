import pytest


@pytest.fixture(scope='session')
def splinter_webdriver():
    return 'phantomjs'

def test_visit_google(browser):
    browser.visit('http://www.google.com')
