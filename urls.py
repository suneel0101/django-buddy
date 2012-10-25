from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings

from starterapp.views import LandingView, logout, home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', LandingView.as_view(), name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^home/$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

# Path to static assets
media_root = {'document_root': settings.MEDIA_ROOT}
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', media_root),
)
