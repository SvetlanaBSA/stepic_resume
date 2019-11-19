import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    browser = webdriver.Chrome()
    if language == "en":
        print("\nstart browser with en language for test..")
    elif language == "ru":
        print("\nstart browser with ru language for test..")
    else:
        raise pytest.UsageError("--language should be en or ru")
    if language == "es" or language == "fr":
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()