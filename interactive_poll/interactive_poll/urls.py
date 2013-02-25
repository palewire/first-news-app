from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', view='polls.views.index', name='polls_index_view'),
    url(r'^polls/(?P<poll_id>\d+)/$', view='polls.views.detail',
        name='polls_detail_view'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', view='polls.views.vote',
        name='polls_vote_view'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
