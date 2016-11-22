from django.conf.urls import url
from foody import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^foody/$', views.snippet_list),
    url(r'^foody/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
