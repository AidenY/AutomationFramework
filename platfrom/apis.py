from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from PlatformModel import serializers
from PlatformModel.models import TestObjects, TestConfig, TestCase
from platfrom.automation import setting
from platfrom.automation.logger import AutoLogger


@api_view(['GET'])
def get_test_cases(request: HttpRequest):
    result = []
    test_cases = TestCase.objects.all()
    for test_case in test_cases:
        serializer = serializers.TestCaseSerializer(test_case)
        result.append(serializer.data)
    return Response(result)


@api_view(['GET', 'POST', 'DELETE'])
def test_object(request):
    method = request.method
    if method == "POST":
        return add_test_object(request)
    elif method == "GET":
        return get_test_objects()
    elif method == "DELETE":
        return delete_test_object(request)
    else:
        return JsonResponse({"error": "unsupported method [" + method + "]"})


@api_view(['GET', 'POST', 'DELETE'])
def test_config(request):
    method = request.method
    if method == "POST":
        return add_test_config(request)
    elif method == "GET":
        return get_test_config()
    elif method == "DELETE":
        return delete_test_config(request)
    else:
        return JsonResponse({"error": "unsupported method [" + method + "]"})


@api_view(['GET', 'POST', 'DELETE'])
def test_case(request):
    method = request.method
    if method == "POST":
        return add_test_testcase(request)
    elif method == "GET":
        return get_test_testcase()
    elif method == "DELETE":
        return delete_test_case(request)
    else:
        return JsonResponse({"error": "unsupported method [" + method + "]"})


def get_test_testcase():
    result = []
    test_objects = TestCase.objects.all()
    for obj in test_objects:
        serializer = serializers.TestCaseSerializer(obj)
        json = serializer.data
        result.append(json)
    return Response(result)


def add_test_testcase(request):
    test_case_name = request.POST['test_case_name']
    name = request.POST['name']
    action = request.POST['action']
    args = request.POST['args']
    serializer = serializers.TestCaseSerializer(
        data={"test_case_name": test_case_name, "name": name, "action": action, "args": args})
    if serializer.is_valid():
        serializer.save();
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


def delete_test_case(request):
    parsed_id = request.POST['id']
    TestCase.objects.filter(id=parsed_id).delete()
    return JsonResponse(data={"status": "delete success"}, status=204)
    pass


def get_test_objects():
    result = []
    test_objects = TestObjects.objects.all()
    for obj in test_objects:
        serializer = serializers.TestObjectsSerializer(obj)
        json = serializer.data
        result.append(json)
    return Response(result)


def add_test_object(request):
    page = request.POST['page']
    name = request.POST['name']
    value = request.POST['value']
    serializer = serializers.TestObjectsSerializer(data={"page": page, "name": name, "value": value})
    if serializer.is_valid():
        serializer.save();
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


def delete_test_object(request):
    parsed_id = request.POST['id']
    TestObjects.objects.filter(id=parsed_id).delete()
    return JsonResponse(data={"status": "delete success"}, status=204)
    pass


def get_test_config():
    result = []
    test_configs = TestConfig.objects.all()
    for config in test_configs:
        serializer = serializers.TestConfigSerializer(config)
        result.append(serializer.data)
    return Response(result)


def add_test_config(request):
    key = request.POST['key']
    value = request.POST['value']
    serializer = serializers.TestConfigSerializer(data={"key": key, "value": value})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)


def delete_test_config(request):
    parsed_id = request.POST['id']
    TestConfig.objects.filter(id=parsed_id).delete()
    return JsonResponse(data={"status": "delete success"}, status=204)


@api_view(['GET'])
def log(request):
    contents = setting.log_capture_string.getvalue()
    return JsonResponse({"log": contents})


@api_view(['GET'])
def get_defined_actions(request):
    return JsonResponse(
        {"result": [setting.action_click, setting.action_sendkeys, setting.action_select, setting.action_select]})


@api_view(['GET'])
def get_all_object_names(request):
    all_object_names = []
    all_objects = TestObjects.objects.all()
    for obj in all_objects:
        serializer = serializers.TestObjectsSerializer(obj)
        json = serializer.data
        name = json['name']
        all_object_names.append(name);
    return JsonResponse({"result": all_object_names})
