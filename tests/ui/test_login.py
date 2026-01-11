from pages.test_task_login_page import LoginPage
from pages.test_task_welcome_page import WelcomePage
from playwright.sync_api import Page

def test_login_with_valid_creds(page: Page) -> None:
    login_page = LoginPage(page)
    welcome_page = WelcomePage(page)
    page.goto("https://the-internet.herokuapp.com/login")
    login_page.wait_until_login_element_displayed(page)
    login_page.login("tomsmith", "SuperSecretPassword!")
    welcome_page.wait_until_flash_message_element_displayed(page)
    welcome_page.is_welcome_message_visible("You logged into a secure area!")

def test_login_with_invalid_password(page: Page) -> None:
    login_page = LoginPage(page)
    welcome_page = WelcomePage(page)
    page.goto("https://the-internet.herokuapp.com/login")
    login_page.wait_until_login_element_displayed(page)
    login_page.login("tomsmith", "invalidpassword")
    welcome_page.wait_until_flash_message_element_displayed(page)
    welcome_page.is_incorrect_password_message_visible("Your password is invalid!")

def test_login_with_invalid_username(page: Page) -> None:
    login_page = LoginPage(page)
    welcome_page = WelcomePage(page)
    page.goto("https://the-internet.herokuapp.com/login")
    login_page.wait_until_login_element_displayed(page)
    login_page.login("invalidusername", "SuperSecretPassword!")
    welcome_page.wait_until_flash_message_element_displayed(page)
    welcome_page.is_incorrect_username_message_visible("Your username is invalid!")