from seleniumBase import SeleniumBase
from selenium_task_3.LocatorsTask3 import Locators
from selenium.webdriver.remote.webelement import WebElement


class PageForTask3(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_name_input_field(self) -> WebElement:
        return self.is_present('xpath', Locators.first_name)

    def get_last_name_input_field(self) -> WebElement:
        return self.is_present('xpath', Locators.last_name)

    def get_phone_input_filed(self) -> WebElement:
        return self.is_present('xpath', Locators.phone)

    def get_email_input_field(self) -> WebElement:
        return self.is_present('id', Locators.email)

    def get_address_input_filed(self) -> WebElement:
        return self.is_present('xpath', Locators.address)

    def get_city_input_field(self) -> WebElement:
        return self.is_present('xpath', Locators.city)

    def get_state_input_filed(self) -> WebElement:
        return self.is_present('xpath', Locators.state)

    def get_postal_code_input_value(self) -> WebElement:
        return self.is_present('xpath', Locators.postal_code)

    def get_click_country_drop_down(self) -> None:
        return self.is_present('xpath', Locators.country_drop_down).click()

    def get_user_name_input_field(self) -> WebElement:
        return self.is_present('id', Locators.user_name)

    def get_password_input_value(self) -> WebElement:
        return self.is_present('xpath', Locators.password)

    def get_confirm_password_input_value(self) -> WebElement:
        return self.is_present('xpath', Locators.confirm_password)

    def get_submit_btn(self) -> None:
        return self.is_present('xpath', Locators.submit_btn).click()

    def get_result_first_last_name(self) -> WebElement:
        return self.is_present('xpath', Locators.first_last_name)

    def get_result_user_name(self) -> WebElement:
        return self.is_present('xpath', Locators.user_name_res)