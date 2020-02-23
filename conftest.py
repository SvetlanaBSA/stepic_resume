import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or ru")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    if language == "en":
        print("\nstart browser with en language for test..")
    elif language == "ru":
        print("\nstart browser with ru language for test..")
    else:
        raise pytest.UsageError("--language should be en or ru")
    if language == "en" or language == "ru":
        link = f"http://selenium1py.pythonanywhere.com/{language}"
        browser.get(link)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()