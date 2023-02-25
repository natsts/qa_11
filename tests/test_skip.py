import pytest
from selene.support.shared import browser
from model.page_github import sign_in_github_desktop, sign_in_github_mobile, assert_main_page_github


@pytest.mark.parametrize(["width", "height"],
                         [(1250, 1250), (390, 890)],
                          ids=["desktop (1250x1250)", "mobile (390x890)"])
def test_github_desktop(width, height):
    if width == 390:
        pytest.skip("Skipped test for desktop, because width of screen 390px")
    else:
        browser.config.window_width = width
        browser.config.window_height = height

        browser.open('https://github.com/')
        sign_in_github_desktop()
        assert_main_page_github()


@pytest.mark.parametrize(["width", "height"],
                         [(1250, 1250), (390, 890)],
                          ids=["desktop (1250x1250)", "mobile (390x890)"])
def test_github_mobile(width, height):
    if width == 1250:
        pytest.skip("Skipped test for mobile, because width of screen 1250px")
    else:
        browser.config.window_width = width
        browser.config.window_height = height

        browser.open('https://github.com/')
        sign_in_github_mobile()
        assert_main_page_github()
