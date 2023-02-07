import pytest

from pages.playwright_home_page import PlaywrightHomePage
from pages.playwright_languages_page import PlaywrightLanguagesPage


class TestSearch:
    @pytest.mark.parametrize('keyword', ['python'])
    def test_search(self,
                    keyword: str,
                    playwright_home_page: PlaywrightHomePage,
                    playwright_languages_page: PlaywrightLanguagesPage
                    ):
        playwright_home_page.visit(playwright_home_page.URL)
        playwright_home_page.navbar.open_search()
        playwright_home_page.navbar.search_modal.perform_search(keyword)
        playwright_home_page.navbar.search_modal.click_search_result(0)

        playwright_languages_page.verify_that_language_title_is_present(keyword)
