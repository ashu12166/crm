from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^message_board/$', views.message, name='list'),

]