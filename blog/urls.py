from django.conf.urls import url, include
from django.contrib import admin


from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'about/', views.about, name='about'),
	url(r'news/$', views.news, name='news'),
	url(r'^news/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^news/new/$', views.post_new, name='post_new'),
	url(r'^news/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^news/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]
