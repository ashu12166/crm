from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^message_board/$', views.message, name='list'),
    url(r'^message_board/post_new$', views.post_new, name='post_new'),
    #url(r'^message_board/post_detail$', views.post_detail, name='post_detail')
    url(r'^message_board/post_detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
