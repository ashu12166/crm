from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='search'),
    url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
    

]