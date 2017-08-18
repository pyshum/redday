from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
	url(r'articles/$', views.articles, name='articles'),
	url(r'article/(?P<article_id>\d+)/$', views.article, name='article'),
	url(r'article/addcomment/(?P<article_id>\d+)/$', views.addcomment, name='addcomment'),
]