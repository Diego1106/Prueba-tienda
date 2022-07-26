from django.urls import re_path
from peticiones import views 
 
urlpatterns = [ 
    re_path(r'^api/peticiones$', views.pqrs_list),
    re_path(r'^api/peticiones/(?P<pk>[0-9]+)$', views.pqrs_detail),
    re_path(r'^api/peticiones/published$', views.pqrs_list_published)
]