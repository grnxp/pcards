from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cards.views',
    # Examples:
    # url(r'^$', 'xcards.views.home', name='home'),
    # url(r'^xcards/', include('xcards.foo.urls')),

	url(r'^details/(?P<card_id>\d+)/$', 'details', name='card-details'),
	url(r'^query/$', 'query'),
	url(r'^advanced-query/$', 'advanced_query', name='advanced-query'),
	url(r'^list/country/(?P<country_id>\d+)/$', 'search_by_country', name='list-by-country'),
	url(r'^list/tag/(?P<tag_id>\d+)/$', 'search_by_tag', name='list-by-tag'),
	url(r'^charts/$', 'charts', name='charts'),
	url(r'^tags/$', 'tags', name='tags'),
	url(r'^about/$', 'about', name='about'),
	url(r'^$', 'index', name='index'),
)

urlpatterns += patterns('osm.views',
	url(r'^map/$', 'map', name='map'),
)
	
urlpatterns += patterns('',	
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),		
)

urlpatterns += staticfiles_urlpatterns()
