from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from . import setting
from .logger import AutoLogger


class ObjectHelper():
    logger = AutoLogger.getLogger()

    def __init__(self, driver: webdriver):
        self.driver: WebDriver = driver

    def find_element(self, value: str):

        try_type = [By.ID, By.NAME, By.XPATH, By.LINK_TEXT, By.TAG_NAME, By.CLASS_NAME, By.CSS_SELECTOR]
        for type in try_type:
            element = self.find_element_by(by=type, value=value)
            if element is not None:
                return element
        return None

    def find_element_by(self, by, value: str, wait_time=setting.default_try_timeout) -> WebElement:
        self.driver.implicitly_wait(wait_time)
        try:
            element = self.driver.find_element(by=by, value=value)
            self.logger.debug("Tried: Element find by " + by + " for value [" + value + "]")
            return element;
        except NoSuchElementException:
            self.logger.debug("Tried: Cannot find the element [" + value + "] by [" + by + "]")
            return None;
        finally:
            self.driver.implicitly_wait(setting.default_timeout)

    def wait_element_exists(self, value: str):
        for i in range(setting.max_timeout):
            self.logger.debug("Wait element exists, tried [" + str(i) + "]")
            element = self.find_element(value)
            if element is not None:
                self.logger.info("Elment found for [" + value + "]")
                return element
        return None

    def wait_element_enable(self, value: str):
        for i in range(setting.max_timeout):
            element = self.wait_element_exists(value)
            if element.is_enabled():
                self.logger.info("Element enable for operating for [" + value + "] ")
                return element
        return None
