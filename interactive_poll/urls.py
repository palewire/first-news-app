from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', view='polls.views.index', name='polls_index'),
    url(r'^polls/(?P<poll_id>\d+)/$', view='polls.views.detail', name='polls_detail'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', view='polls.views.vote', name='polls_vote'),
    url(r'^local-media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT, 'show_indexes': True
    }),
)
