from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.text import Text


class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.no_results_title = Text(page, '//p[@class="DocSearch-Title" and contains(text(), "No results for")]',
                                     'No results')
        self.search_input = Input(page, '#docsearch-input', 'Search docs')
        self.search_result = ListItem(page, '#docsearch-item-{result_number}', 'Result Item')

    def verify_that_modal_is_open(self):
        self.search_input.should_be_visible()

    def perform_search(self, keyword: str) -> None:
        self.search_input.fill(keyword, validate_value=True)

    def click_search_result(self, result_number: int) -> None:
        self.search_result.click(result_number=result_number)
