import pytest
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
from playwright.sync_api import Page

@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
        ("tomsmith", "invalidpassword", "Your password is invalid!"),
        ("invalidusername", "SuperSecretPassword!", "Your username is invalid!"),
    ],
    ids=[
        "valid-login",
        "invalid-password",
        "invalid-username",
    ]
)

def test_login(page: Page, username: str, password: str, expected_message: str) -> None:
    login_page = LoginPage(page)
    welcome_page = WelcomePage(page)

    page.goto("https://the-internet.herokuapp.com/login")
    login_page.login(username, password)

    welcome_page.assert_flash_message(expected_message)