from seleniumBase import SeleniumBase
from selenium_task_2.LocatorsTask2 import Locators
from selenium.webdriver.remote.webelement import WebElement


class PageForTask2(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def get_select_value_field(self) -> WebElement:
        return self.is_present('xpath', Locators.select_value_xpath)

    def get_group_1_option_2_value(self) -> None:
        return self.is_present('xpath', Locators.group_1_option_2_xpath).click()

    def get_select_one_field(self) -> None:
        return self.is_present('xpath', Locators.select_one_xpath).click()

    def get_dr_value(self) -> None:
        return self.is_present('xpath', Locators.dr_xpath).click()

    def get_old_style_field(self) -> WebElement:
        return self.is_present('id', Locators.old_style_select_menu_id)

    def get_standard_multi_field(self) -> WebElement:
        return self.is_present('id', Locators.standard_multi_select_id)

