import pytest
from selene.support.shared import browser
from model.page_github import sign_in_github_desktop, assert_main_page_github, sign_in_github_mobile


@pytest.mark.parametrize("browser_size", ["desktop"], indirect=True)
def test_github_desktop(browser_size):
    browser.open('https://github.com/')
    sign_in_github_desktop()
    assert_main_page_github()


@pytest.mark.parametrize("browser_size", ["mobile"], indirect=True)
def test_github_mobile(browser_size):
    browser.open('https://github.com/')
    sign_in_github_mobile()
    assert_main_page_github()
