from rest_framework import serializers

from . import models


class TestObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestObjects
        fields = ('id', 'page', 'name', 'value')


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestCase
        fields = ("id", "test_case_name", "name", "action", "args")


class TestConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestConfig
        fields = ("id", "key", "value")
