from seleniumBase import SeleniumBase
from selenium_task_4.LocatorsTask4 import LocatorsForButton, LocatorsForFeedback
from selenium.webdriver.remote.webelement import WebElement


class PageForButtonClick4(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def get_click_button(self) -> None:
        return self.is_present('xpath', LocatorsForButton.BUTTON_XPATH).click()


class PageForFeedBack4(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def get_name_input_field(self) -> WebElement:
        return self.is_present('xpath', LocatorsForFeedback.NAME_INPUT_FIELD_XPATH)

    def get_message_input_field(self) -> WebElement:
        return self.is_present('xpath', LocatorsForFeedback.MESSAGE_INPUT_VALUE_XPATH)

    def get_submit_btn(self) -> None:
        return self.is_present('xpath', LocatorsForFeedback.SUBMIT_BTN_XPATH).click()

    def get_successful_text(self) -> WebElement:
        return self.is_present('xpath', LocatorsForFeedback.THANKS_FOR_CONTACTING_US_XPATH)

    def get_please_fill(self) -> WebElement:
        return self.is_present('xpath', LocatorsForFeedback.PLEASE_FILL_IN_THE_FOLLOWING_FIELD_XPATH)

    def get_message_world(self) -> WebElement:
        return self.is_present('xpath', LocatorsForFeedback.MESSAGE_INPUT_VALUE_XPATH)
