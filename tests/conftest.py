from selene.support.shared import browser
import pytest


@pytest.fixture()
def set_desktop_browser():
    browser.config.window_width = 1400
    browser.config.window_height = 800
    yield
    browser.quit()


@pytest.fixture()
def set_mobile_browser():
    browser.config.window_width = 400
    browser.config.window_height = 900
    yield
    browser.quit()


@pytest.fixture(params=['desktop', 'mobile'])
def set_website_window_orientation(request):
    if request.param == 'desktop':
        browser.config.window_width = 1400
        browser.config.window_height = 800
    elif request.param == 'mobile':
        browser.config.window_width = 400
        browser.config.window_height = 900

    return request.param
