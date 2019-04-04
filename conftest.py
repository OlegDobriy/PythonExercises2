from fixture.application import Application
import pytest


fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.check_login(username="Admin", password="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def app_stop(request):

    def final():
        fixture.session.check_logout()
        fixture.destroy()

    request.addfinalizer(final)
    return fixture
