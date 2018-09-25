import configparser
import os

import pandas

from selenium import webdriver

from . import setting
from .action_helper import ActionHelper
from .logger import AutoLogger
from .objecthelper import ObjectHelper


class Core:
    logger = AutoLogger.getLogger()

    def __init__(self, test_cases, test_configs):
        self.driver = webdriver.Chrome()
        self.obj_helper = ObjectHelper(self.driver)
        self.url = str(test_configs['测试地址'])
        self.action_helper = ActionHelper(object_helper=self.obj_helper)
        self.test_configs = test_configs
        self.test_cases = test_cases
        self.do_prepare()

    def load_conf(self):
        conf = "conf/config.conf"
        if os.path.exists(conf):
            self.logger.info("Load config file on [%s]", conf)
            config = configparser.ConfigParser()
            config.read(conf, encoding='utf-8')
            default = config['DEFAULT']
            action_keywords = config['ACTION.KEYWORD']
            setting.default_try_timeout = float(default['DefaultTryTime'])
            setting.default_timeout = int(default['DefaultTimeout'])
            setting.max_timeout = int(default['MaxTimeout'])
            setting.action_click = action_keywords['Click']
            setting.action_sendkeys = action_keywords['SendKeys']
            setting.action_select = action_keywords['Select']
            setting.action_wait_element_display = action_keywords['WaitDisplays']
        else:
            self.logger.info("No config file exists, init default config file on [%s]", conf)
            config = configparser.ConfigParser()
            config['DEFAULT'] = {'DefaultTryTime': 0.4,
                                 'DefaultTimeout': 40,
                                 'MaxTimeout': 90}
            config['ACTION.KEYWORD'] = {'Click': '点击',
                                        'SendKeys': '输入',
                                        'Select': '选择',
                                        'WaitDisplays': '等待元素显示'}
            with open(conf, 'w') as configfile:
                config.write(configfile)

    def init_driver(self):
        if self.url == "":
            df = pandas.read_excel(self.data_path, sheet_name='参数配置')
            self.url = df[df.配置项 == '测试地址'].reset_index().配置值[0]
        self.driver.get(self.url)

    def do_prepare(self):
        if not os.path.exists(setting.log_screenshot_folder):
            os.makedirs(setting.log_screenshot_folder)
        self.init_driver()
        self.load_conf()
        self.test_configs = [setting.action_wait_element_display, setting.action_select, setting.action_sendkeys,
                             setting.action_click]

    def run(self):
        try:
            for test_case in self.test_cases:
                step = test_case['action']
                test_object_name = test_case['name']
                test_object_value = test_case['object_value']
                test_args = test_case['args']
                if test_args == "[]":
                    test_args = []
                else:
                    test_args = [test_args]
                self.action_helper.action(step, test_object_name, test_object_value, test_args)
            self.driver.save_screenshot("test.png")
            self.driver.quit()
        except Exception as e:
            self.logger.error(e)
