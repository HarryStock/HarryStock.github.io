from django.conf.urls import patterns, include, url
from django.contrib import admin
# from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),

    url(r'admin/', include(admin.site.urls)),
    url(r'it/', include('it.urls')),
    url(r'', include('it.urls')),
)
