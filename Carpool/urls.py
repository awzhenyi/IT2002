from . import views
from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns    

urlpatterns=[
    re_path(r'^$', views.index),
    re_path(r'Results',views.result),
    re_path(r'register',views.register, name = 'register'),
    re_path(r'success', views.success),
    re_path(r'index',views.index),
    re_path(r'login',views.login),
    re_path(r'DriverAddRequest',views.DriverAddRequest,name='DriverAddRequest'),
    re_path(r'RiderAddRequest',views.RiderAddRequest),
    #path('temp/<str:pk>/',views.temp,name='udar'),
    re_path(r'^temp/(?P<pk>[\w\-]+)/$',views.temp,name='udar'),
    re_path(r'confirm',views.confirm),
    re_path(r'logout',views.logout),
    re_path(r'home',views.home)
]

urlpatterns += staticfiles_urlpatterns()