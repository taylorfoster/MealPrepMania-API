from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from foody import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^groceryList/$', views.groceryList_list),
    url(r'^groceryList/(?P<pk>[0-9]+)$', views.groceryList_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
