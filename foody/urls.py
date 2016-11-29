from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from foody import views

urlpatterns = [
    url(r'^recipes/$', views.recipe_list),
    url(r'^recipes/(?P<pk>[0-9]+)$', views.recipe_detail),
    url(r'^groceryList/$', views.groceryList_list),
    url(r'^groceryList/(?P<pk>[0-9]+)$', views.groceryList_detail),
    url(r'^menu/$', views.menu_list),
    url(r'^menu/(?P<pk>[0-9]+)$', views.menu_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
