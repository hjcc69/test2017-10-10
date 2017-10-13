from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'product/(?P<pk>\d+)/$', views.show, name='show'),
    url(r'comment/create', views.comment, name='comment'),



]