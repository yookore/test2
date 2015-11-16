from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from su_app.views import *

status_list = StatusUpdateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = patterns('',
    # Examples:
    url(r'^api/v1/statusupdates/$', status_list, name='statusupdates'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home, name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
