from selene.support.conditions import have
from selene.support.shared import browser
import pytest


@pytest.mark.parametrize('set_website_window_orientation', ['desktop'], indirect=True)
def test_github_desktop_with_indirect(set_website_window_orientation):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-header p-0']").should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('set_website_window_orientation', ['mobile'], indirect=True)
def test_github_mobile_with_indirect(set_website_window_orientation):
    browser.open('https://github.com/')
    browser.element("[class='Button-label']").click()
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-header p-0']").should(have.text('Sign in to GitHub'))