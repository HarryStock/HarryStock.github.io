from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
urlpatterns = [

    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit),
    url(r'^(?P<language>[A-Z][a-z]*)/$', views.language),
    url(r'^/(?P<topic>[A-Z][a-z]*)/$', views.topic),
    url(r'^(?P<language>[A-Z][a-z]*)/(?P<topic>[A-Z][a-z]*)/$', views.item),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.all_posts),
]

