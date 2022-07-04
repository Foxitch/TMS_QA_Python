from selenium.webdriver.remote.webelement import WebElement
from seleniumBase import SeleniumBase
from selenium_task_5.LocatorsTask5 import LocatorsTask5


class PageForButtonClick5(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def get_checkbox_click(self) -> None:
        return self.is_present('xpath', LocatorsTask5.CHECKBOX).click()

    def validate_checkbox_is_disappeared(self) -> bool:
        return self.invisibility_of_element('xpath', LocatorsTask5.CHECKBOX)

    def get_remove_btn(self) -> None:
        return self.is_present('xpath', LocatorsTask5.REMOVE_BTN).click()

    def get_its_gone_text(self) -> str:
        return self.is_present('xpath', LocatorsTask5.ITS_GONE).text

    def get_input_field(self) -> WebElement:
        return self.is_present('xpath', LocatorsTask5.INPUT_FILED)

    def get_enable_btn(self) -> None:
        return self.is_present('xpath', LocatorsTask5.ENABLE_BTN).click()

    def get_its_enabled_text(self) -> str:
        return self.is_present('xpath', LocatorsTask5.ITS_ENABLED).text
