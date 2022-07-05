from selenium.webdriver.remote.webelement import WebElement
from seleniumBase import SeleniumBase
from selenium_task_6.LocatorsTask6 import LocatorsTask6


class PageForButtonClick6(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def get_iframe_btn(self) -> None:
        return self.is_present('xpath', LocatorsTask6.IFRAME_BTN_XPATH).click()

    def __get_frame_element(self) -> WebElement:
        return self.is_present('tag_name', LocatorsTask6.IFRAME_TAG_NAME)

    def switch(self):
        return self.switch_to_iframe(self.__get_frame_element())

    def get_text(self) -> str:
        return self.is_present('xpath', LocatorsTask6.TEXT_XPATH).text
