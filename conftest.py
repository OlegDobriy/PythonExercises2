from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture(scope='session')
# scope указывает, что браузер запускается один раз на всю сессию,
# а не каждый раз заново
def app(request):
    fixture = Application()
    fixture.session.login(username="Admin", password="secret")

    def final():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(final)
    return fixture
