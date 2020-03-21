import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):

    # it is not necessary to parser different drivers in this step
    parser.addoption("--driver_name",
                     action="store",
                     default="chrome",
                     help="Choose driver: chrome or firefox")

    parser.addoption("--language",
                     action="store",
                     default="en",
                     help="Choose language: en, es, ru etc.")


@pytest.fixture(scope="function")
def driver(request):

    driver_name = request.config.getoption("driver_name")
    user_language = request.config.getoption("language")

    if driver_name == "chrome":
        print("\n--- start chrome driver for test---")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)

    # this selection may be omitted, since it clarified that only Chrome browser should be checked
    elif driver_name == "firefox":
        print("\n--- start firefox driver for test---")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--driver_name should be 'chrome' or 'firefox'")

    yield driver
    print("\n--- quit driver ---")
    driver.quit()
