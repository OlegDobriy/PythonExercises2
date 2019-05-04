from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        path_to_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(path_to_config_file) as config_file:
            target = json.load(config_file)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    baseUrl = request.config.getoption('--baseUrl')
    web_config = load_config(request.config.getoption('--target'))['web']  # открыть конфиг из json, часть с web
    if baseUrl is None:  # если задали URL в параметре запуска, то брать его, иначе брать из target.json
        baseUrl = web_config['baseUrl']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=baseUrl)
    fixture.session.check_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']  # открыть конфиг из json, часть с db
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def final():
        dbfixture.destroy()
    request.addfinalizer(final)
    return dbfixture


@pytest.fixture(scope='session', autouse=True)
def app_stop(request):
    def final():
        fixture.session.check_logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption('--check_ui')


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--baseUrl', action='store')
    parser.addoption('--target', action='store', default='target.json')
    parser.addoption('--check_ui', action='store_true')


def pytest_generate_tests(metafunc):  # задаем, как в функциях будет называться параметр, в котором передаются
    for fixture in metafunc.fixturenames:  # тестовые данные
        if fixture.startswith('data_'):
            testdata = load_from_module(fixture[5:])  # убрать первые пять символов (data_)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        if fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])  # убрать первые пять символов (json_)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.json' % file)) as f:
        return jsonpickle.decode(f.read())
