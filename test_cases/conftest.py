import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="specify the browser to use")

@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    return browser

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Unknown browser %s" % browser)
    return driver

############### FOR PYTEST HTML REPORTS #########
#Hook for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Ecommerce, nopcommerce'
    config.stash[metadata_key] ['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key] ['Tester Name'] = 'Saritha'

#Hook for delete/modify environment info in html report
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)