# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 03:04:34 2017

@author: ROZIN
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]