import io
import pandas
import threading

from django.http import HttpResponse, JsonResponse
from numpy import NaN
from rest_framework.response import Response

from PlatformModel import models, serializers
from PlatformModel.models import TestObjects, TestConfig, TestCase
from platfrom.automation import core, setting


def run_auto(test_cases, test_configs):
    print("Start run automation")
    core.Core(test_cases, test_configs).run();
    # setting.reset_log_capture_string()
    setting.log_capture_string.seek(0, 0)
    setting.log_capture_string.truncate()
    # setting.log_capture_string= io.StringIO();
    print("End Run automation")
    pass


def run(request):
    test_cases = []
    cases = TestCase.objects.all();
    for case in cases:
        serializer = serializers.TestCaseSerializer(case)
        n_object = TestObjects.objects.get(name=str(case.name))
        object_value = serializers.TestObjectsSerializer(n_object).data['value']
        json = serializer.data
        json['object_value'] = object_value
        test_cases.append(json)

    test_configs = {}
    configs = TestConfig.objects.all();
    for config in configs:
        serializer = serializers.TestConfigSerializer(config)
        test_configs[serializer.data['key']] = serializer.data['value']
    print(test_configs)
    threading.Thread(target=run_auto(test_cases=test_cases, test_configs=test_configs), name='run auto')
    return HttpResponse(test_cases);

    # data_path = '初始化文档.xlsx'
    # core.Core(data_path=data_path).run()

    # return HttpResponse("Completed")


def init_config(config_data):
    # remove all
    configs = TestConfig.objects.all()
    for config in configs:
        print("remove for [" + config.key + "]")
        config.delete()

    arr_key = list(config_data['配置项'])
    arr_value = list(config_data['配置值'])
    for i, key in enumerate(arr_key):
        value = arr_value[i];
        serializer = serializers.TestConfigSerializer(data={"key": key, "value": value})
        if serializer.is_valid():
            serializer.save()
        print("save for key [" + key + "]")


def init_case(step_data):
    # remove all

    step_data = step_data.where(step_data.notnull(), "[]")
    cases = TestCase.objects.all()
    for case in cases:
        print("remove for [" + case.name + "]")
        case.delete()

    arr_name = list(step_data['测试对象'])
    arr_action = list(step_data['测试动作'])
    arr_args = list(step_data['测试辅助值'])
    for i, name in enumerate(arr_name):
        action = arr_action[i];
        args = arr_args[i]
        serializer = serializers.TestCaseSerializer(data={"name": name, "action": action, "args": args})
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.error_messages)
        print("save for name [" + name + "]")


def init_object(object_data):
    # remove all
    print("Init for test objects")
    objects = TestObjects.objects.all()
    for obj in objects:
        print("remove for [" + obj.name + "]")
        obj.delete()

    arr_name = list(object_data['名字'])
    arr_value = list(object_data['识别值'])
    for i, name in enumerate(arr_name):
        value = arr_value[i];
        serializer = serializers.TestObjectsSerializer(data={"name": name, "value": value})
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.error_messages)
        print("save for name [" + name + "]")


def init(request):
    i = initdata("conf/初始化文档.xlsx")
    step_data, object_data, config_data = i.read_data()

    init_config(config_data)
    init_case(step_data)
    init_object(object_data)
    return HttpResponse("success")
    pass


class initdata():

    def __init__(self, data_path):
        self.data_path = data_path

    def read_data(self):
        step_data = pandas.read_excel(self.data_path, sheet_name='测试步骤')
        object_data = pandas.read_excel(self.data_path, sheet_name='对象库')
        config_data = pandas.read_excel(self.data_path, sheet_name='参数配置')
        return step_data, object_data, config_data

    def retrieve_datas(self):
        arr_test_steps = []
        step_data, object_data = self.read_data()
        objects = step_data.get('测试对象')
        steps = step_data.get('测试动作')
        add_infos = step_data.get('测试辅助值')
        for i in range(len(objects)):
            step = steps[i];
            test_object_name = objects[i]
            test_object_value = object_data[object_data.名字 == test_object_name].reset_index().识别值[0]
            addi_infos = [add_infos[i]]
            test_step = teststep(step, test_object_name, test_object_value, addi_infos)
            arr_test_steps.append(test_step)
        return arr_test_steps
