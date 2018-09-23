# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.utils.text import Truncator
from tabbed_admin import TabbedModelAdmin

from .models import Article
# Register your models here.


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
#
#
# def truncated_name(obj):
#     name = '{0}'.format(obj.article_text)
#     return Truncator(name).chars(120)


@admin.register(Article)
class ArticleAdmin(TabbedModelAdmin):
    form = ArticleAdminForm

    list_display = ('article_title', 'article_text', 'article_date', 'article_likes', 'timestamp')
    list_per_page = 5

    search_fields = ('article_title', )

