from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.webdriver = webdriver
        self.__wait = WebDriverWait(driver, 10)

    @staticmethod
    def __get_selenium_by(find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def save_screenshot(self, path):
        return self.driver.save_screenshot(path)

    def current_url(self):
        current_url = self.driver.current_url
        return current_url

    def move_to_url(self, url: str):
        return self.driver.get(url)

    @staticmethod
    def get_element_attribute(element: WebElement, attribute_name: str):
        return element.get_attribute(attribute_name)

    def is_present(self, find_by, locator, locator_name=None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by, locator, locator_name=None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

