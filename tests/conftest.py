import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_desktop():
    browser.config.window_width = 1250
    browser.config.window_height = 1250


@pytest.fixture()
def browser_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 890


@pytest.fixture(params=['desktop', 'mobile'])
def browser_size(request):
    if request.param == 'desktop':
        browser.config.window_width = 1250
        browser.config.window_height = 1250
    elif request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 890
