import allure
import logging

from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'button'

    def hover(self, **kwargs) -> None:
        with allure.step(f'Hovering over {self.type_of} with name {self.name}'):
            locator = self.get_locator(**kwargs)
            locator.hover()
            logging.info(f'Hovering over {self.type_of} with name {self.name}')

    def double_click(self, **kwargs) -> None:
        with allure.step(f'Double clicking {self.type_of} with  name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.dblclick()