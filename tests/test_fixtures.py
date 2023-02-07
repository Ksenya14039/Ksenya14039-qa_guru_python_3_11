from selene.support.conditions import have
from selene.support.shared import browser


def test_sign_in_desktop_with_fixtures(set_desktop_browser):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-header p-0']").should(have.text('Sign in to GitHub'))


def test_sign_in_mobile_with_fixture(set_mobile_browser):
    browser.open('https://github.com/')
    browser.element("[class='Button-label']").click()
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-header p-0']").should(have.text('Sign in to GitHub'))