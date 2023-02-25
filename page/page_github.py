from selene import have
from selene.support.shared import browser


def sign_in_github_desktop():
    browser.element('[href="/login"]').click()


def sign_in_github_mobile():
    browser.element('.Header-old .container-xl .d-flex [aria-label="Toggle navigation"]').click()
    browser.element('[href="/login"]').click()


def assert_main_page_github():
    assert browser.element('.auth-form-header h1').should(have.exact_text('Sign in to GitHub'))
