import json

from .automation.entities import testobject, teststep, config
from . import values


class dataloader():

    def __init__(self):
        pass

    def load(self):
        self.load_objects();
        self.load_testcase();
        self.load_conf();

    def find_object_value(self, test_object_name):
        for obj in values.testobjects:
            if obj.test_object_name == test_object_name:
                return obj.test_object_value

    def load_objects(self):
        with open("management/objectrepository.json", 'r', encoding='utf-8') as load_f:
            test_objects = json.load(load_f)
            print(test_objects)
            # print(load_dict)
        for test_object in test_objects:
            values.testobjects.append(
                testobject(test_object_name=test_object['对象名称'], test_object_value=test_object['识别值']))

    def load_testcase(self, testcase_file="management/testcase.json"):
        with open(testcase_file, 'r', encoding='utf-8') as load_f:
            tc = json.load(load_f)

        for ts in tc:
            action = str(ts.get("测试动作"))
            test_object_name = ts['测试对象']
            test_object_value = self.find_object_value(test_object_name=test_object_name)
            addition_infos = ts['测试辅助值']
            values.testcase.append(
                teststep(step=action, test_object_name=test_object_name, test_object_value=test_object_value,
                         addition_infos=addition_infos))

    def load_conf(self):
        with open("management/config.json", 'r', encoding='utf-8') as load_f:
            t = json.load(load_f)
            print(values.config)

        for v in t:
            values.config.append(config(key=v['配置项'], value=v['配置值']))
