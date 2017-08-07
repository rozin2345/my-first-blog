# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 01:59:51 2017

@author: ROZIN
"""

from django import forms

from .models import Post

class PostForm (forms.ModelForm):

	class Meta:

		model = Post
		fields = ('title', 'text',)