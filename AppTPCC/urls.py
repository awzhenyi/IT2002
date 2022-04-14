from . import views
from django.urls import path, re_path

urlpatterns=[
    re_path(r'^$', views.index),
    re_path(r'result', views.result),
    re_path(r'query', views.query, name = 'query'),
    re_path(r'report', views.report),
    re_path(r'test', views.test, name = 'test'),
    re_path(r'visualise', views.visualise),
]

