from __future__ import annotations

import allure
from playwright.sync_api import Page, Response


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def visit(self, url: str) -> Response | None:
        with allure.step(f'Opening the URL "{url}"'):
            return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with URL "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')
