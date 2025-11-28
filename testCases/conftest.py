from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    return driver


def pytest_adoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_(confiig):
    confiig._metadata['Project Name'] = 'Nop Commerce'
    confiig._metadata['Module Name'] = 'Customer'
    confiig._metadata['Tester Name'] = 'Kiran'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_home", None)
    metadata.pop("Plugins", None)
