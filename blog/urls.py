# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 03:04:34 2017

@author: ROZIN
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name ='post_new'),
     url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]