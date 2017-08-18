# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
	article_title = models.CharField(max_length=200)
	article_text = models.TextField()
	article_date = models.DateTimeField()
	article_likes = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)


class Comments(models.Model):
	comments_text = models.TextField()
	comments_article = models.ForeignKey(Article)
	comments_author = models.CharField(max_length=120)
