from django.db import models

# Create your models here.
ALL = 'ALL'


class TestCase(models.Model):
    id = models.AutoField(primary_key=True)
    test_case_name = models.CharField(max_length=20, default="默认", null=True)
    name = models.CharField(max_length=20)
    action = models.CharField(max_length=100)
    args = models.CharField(max_length=300, null=True, default='')


class TestObjects(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.CharField(max_length=20, default='ALL', null=True)
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=100)
    # name = models.ForeignKey(TestCase, related_name='name', on_delete=models.DO_NOTHING)
    pass


class TestConfig(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=300)
