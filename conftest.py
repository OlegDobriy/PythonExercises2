from fixture.application import Application
import pytest
import json
import os.path


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    baseUrl = request.config.getoption('--baseUrl')
    if target is None:  # загружать конфиг только один раз
        path_to_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),  # чтобы каждый раз не указы-
                                               request.config.getoption('--target'))        # вать путь к файлу с конф.
        with open(path_to_config_file) as config_file:
            target = json.load(config_file)  # прочитать json с конфигурацией
    if baseUrl is None:  # если задали URL в параметре запуска, то брать его, иначе брать из target.json
        baseUrl = target['baseUrl']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=baseUrl)
    fixture.session.check_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def app_stop(request):

    def final():
        fixture.session.check_logout()
        fixture.destroy()

    request.addfinalizer(final)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--baseUrl', action='store')
    parser.addoption('--target', action='store', default='target.json')
