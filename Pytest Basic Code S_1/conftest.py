import pytest



# @pytest.fixture(scope="function", autouse=True)
# @pytest.fixture(autouse=True)
@pytest.fixture(scope="session", autouse=True)

def tc_setup(browser):
    if browser == "chrome":
        print("launch chrome")
    elif browser == "ff":
        print("Launch firefox")
    else:
        print("Provide valid browser")

    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

#pytest -v -s -- browser chrome/ff