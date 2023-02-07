from playwright.sync_api import Page

from components.modals.search_modal import SearchModal
from page_factory.button import Button
from page_factory.link import Link


class NavBar:
    def __init__(self, page: Page):
        self.page = page

        self.search_modal = SearchModal(page)

        self.docs_link = Link(page, "//a[.='Docs']", 'Docs')
        self.api_link = Link(page, "//a[.='API']", 'API')
        self.search_button = Button(page, "button.DocSearch-Button", 'Search')

    def visit_docs(self):
        self.docs_link.click()

    def visit_api(self):
        self.api_link.click()

    def open_search(self):
        self.search_button.hover()
        self.search_button.click()
        self.search_modal.verify_that_modal_is_open()

