import time
import datetime

import pandas
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select as s

from .entities import teststep
from .objecthelper import ObjectHelper
from . import setting
from .logger import AutoLogger


class Select():
    logger = AutoLogger.getLogger()

    def __init__(self, webelement: WebElement):
        self.webelement = webelement

    def select(self, value):
        select = s(self.webelement)
        value = str(value)
        time.sleep(0.5)
        try:
            self.logger.debug("Tried: select_by_visible_text on [%s]", value)
            select.select_by_visible_text(value)
            return True
        except:
            pass
        try:
            self.logger.debug("Tried: select_by_value on [%s]", value)
            select.select_by_value(value)
            return True
        except:
            pass
        try:
            self.logger.debug("Tried: select_by_index on [%s]", value)
            select.select_by_index(int(value))
            return True
        except:
            pass
        raise NoSuchElementException("Unable select on [%s]", value)


class ActionHelper():
    logger = AutoLogger.getLogger()

    def __init__(self, object_helper: ObjectHelper = None):

        self.obj_helper = object_helper

    def action(self, step, test_object_name, test_object_value, args):
        self.logger.info(
            "action [" + step + "], object [" + test_object_name + "], addition value [" + str(args) + "] ")
        element = None
        if step == setting.action_click:
            self.obj_helper.wait_element_enable(test_object_value).click()
        elif step == setting.action_sendkeys:
            self.obj_helper.wait_element_enable(test_object_value).send_keys(str(args[0])),
        elif step == setting.action_wait_element_display:
            element = self.obj_helper.wait_element_enable(test_object_value)
        elif step == setting.action_select:
            Select(self.obj_helper.wait_element_enable(test_object_value)).select(args[0])
        else:
            self.logger.error("No Action defined for [%s]", step)
        self.obj_helper.driver.save_screenshot(setting.log_screenshot_folder + "/" +
                                               str(test_object_name) + "_" + str(
            step) + "_" + datetime.datetime.now().strftime(
            '%Y-%m-%d-%H-%M') + "_screenshot.png")
        return element
