from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture(scope='session')
# scope указывает, что браузер запускается один раз на всю сессию,
# а не каждый раз заново
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
