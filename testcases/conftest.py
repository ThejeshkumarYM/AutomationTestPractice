import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.readproperties import config


@pytest.fixture
def setup(browser):
    if browser=="edge":
        driver=webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("edge driver initialized")
    elif browser=="firefox":
        driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("firefox driver initialized")
    else:
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("chrome driver initialized")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############# pytest html report #################

# def pytest_configure(config):
#     config._metadata['Project Name']='automation practice'
#     config._metadata['Module Name'] = 'registration'
#     config._metadata['Tester'] = 'Thejesh'
#
# ############### hook, delete previous info ################
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Java_Home",None)
#     metadata.pop("Plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".html"






