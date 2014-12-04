from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^heroku/$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hello.views.Home', name='savemoney-home'),
    url(r'^save/$', 'hello.views.SaveMoneyForm', name='save-submit-form'),
    url(r'^savehistory/$', 'hello.views.ShowHistory', name='show-history-form'),
    url(r'^process_update/$', 'hello.views.ProcessUpdate', name='process-update'),
    url(r'^process_delete/$', 'hello.views.ProcessDelete', name='process-delete'),
    url(r'^login/$', 'hello.views.Login', name='login'),
    url(r'^logout/$', 'hello.views.Logout', name='logout'),
    url(r'^accounts/login/$', 'hello.views.Login', name='login'),
    url(r'^register/$', 'hello.views.Register', name='register'),
)
