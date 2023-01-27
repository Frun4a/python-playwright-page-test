from playwright.sync_api import Page

from page_factory.text import Text
from pages.base_page import BasePage


class PlaywrightLanguagesPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.language_title = Text(page, 'h2#{language}', 'Language title')

    def verify_that_language_title_is_present(self, language: str):
        self.language_title.should_be_visible(language=language)
        self.language_title.should_have_text(language.capitalize(), language=language)

