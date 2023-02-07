from selene.support.conditions import have
from selene.support.shared import browser
import pytest


def test_github_desktop_with_skip(set_website_window_orientation):
    website_view_version = set_website_window_orientation
    if website_view_version == 'mobile':
        pytest.skip('Skip mobile website view version')
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-header p-0']").should(have.text('Sign in to GitHub'))


def test_github_mobile_with_skip(set_website_window_orientation):
    website_view_version = set_website_window_orientation
    if website_view_version == 'desktop':
        pytest.skip('Skip desktop website view version')
    browser.open('https://github.com/')
    browser.element("[class='Button-label']").click()
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-header p-0']").should(have.text('Sign in to GitHub'))