# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Article, Comments
from .forms import CommentForm
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = Article._meta._get_fields()

admin.site.register(Article)
