"""platfrom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import platfrom.apis
import platfrom.views
from . import executor, views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.index),
    url('^run$', executor.run),
    # url('^object-repository', views.object_repository),
    url('^init', executor.init),
    # url('^config', views.conf),
    # url('^add-test-object', platfrom.apis.add_test_object),
    # url('^get-object-names$', platfrom.apis.get_object_names),
    # url('^get-test-cases$', platfrom.apis.get_test_cases),
    # url('^get-test-objects$', platfrom.apis.get_test_objects),

    url('^test-config$', platfrom.apis.test_config),
    url('^test-case', platfrom.apis.test_case),
    url('^test-object', platfrom.apis.test_object),
    url('^log$', platfrom.apis.log),
    url('^get-defined-actions$', platfrom.apis.get_defined_actions),
    url('^get-object-names$', platfrom.apis.get_all_object_names),
]
