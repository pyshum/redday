# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from forms import CommentForm

from .models import Article, Comments

# Create your views here.

def articles(request):
	all_articles = Article.objects.all().order_by("-timestamp")
	paginator = Paginator(all_articles, 2)

	page = request.GET.get('page')
	#pagination
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		#If page is not an integer, deliver first page.
		articles = paginator.page(1)
	except EmptyPage:
		#If page is out of range, deliver last page of result
		articles = paginator.page(paginator.num_pages)

	context = {
	'all_articles': all_articles,
	'articles': articles,
	}
	return render(request, 'comments/articles.html', context)


def article(request, article_id=1):
	args = Article.objects.get(id=article_id)
	comment = Comments.objects.filter(comments_article_id=article_id)
	form = CommentForm(request.POST or None)
	args = {
		'args': args,
		'form': form,
		'comment': comment,
	}
	# args['comments'] = Comments.objects.filter(comments_article_id=article_id)
	# args['form'] = comment_form	
	return render(request, 'comments/article.html/', args)


def addcomment(request, article_id):
	if request.POST and ("pause" not in request.session):
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.comments_article = Article.objects.get(id=article_id)
			form.save()
			request.session.set_expiry(60)
			request.session['pause'] = True
			return redirect('/article/addcomment/%s/' % article_id)
	return HttpResponseRedirect('/article/%s/' % article_id)