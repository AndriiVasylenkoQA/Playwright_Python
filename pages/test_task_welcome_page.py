from playwright.sync_api import Page, expect

class WelcomePage:

    def __init__(self, page:Page):
        self.page = page
        self.flash_message = page.locator("#flash-messages")

    def wait_until_flash_message_element_displayed(self, page:Page):
        self.page = page
        page.locator("#flash-messages").wait_for()

    def is_welcome_message_visible(self, message: str):
        expect(self.flash_message).to_contain_text(message)

    def is_incorrect_password_message_visible(self, message: str):
        expect(self.flash_message).to_contain_text(message)

    def is_incorrect_username_message_visible(self, message: str):
        expect(self.flash_message).to_contain_text(message)

