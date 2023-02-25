from selene.support.shared import browser
from model.page_github import sign_in_github_desktop, assert_main_page_github, sign_in_github_mobile


def test_github_desktop(browser_desktop):
    browser.open('https://github.com/')
    sign_in_github_desktop()
    assert_main_page_github()


def test_github_mobile(browser_mobile):
    browser.open('https://github.com/')
    sign_in_github_mobile()
    assert_main_page_github()
