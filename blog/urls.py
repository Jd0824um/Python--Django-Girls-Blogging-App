from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # Assigns a view called post_list to the ^$ url
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'), #Assigns a view called post_new to the url,
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), # Assigns a view called post_edit to the url

]