from playwright.sync_api import Page, expect

class WelcomePage:

    def __init__(self, page:Page):
        self.page = page
        self.flash_message = page.locator("#flash-messages")

    def assert_flash_message(self, expected_text: str):
        expect(self.flash_message).to_contain_text(expected_text)
