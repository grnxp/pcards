from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xcards.views.home', name='home'),
    # url(r'^xcards/', include('xcards.foo.urls')),

	url(r'^details/(?P<card_id>\d+)/$', 'cards.views.details', name='card-details'),
	url(r'^query/$', 'cards.views.query'),
	url(r'^advanced-query/$', 'cards.views.advanced_query', name='advanced-query'),
	url(r'^list/country/(?P<country_id>\d+)/$', 'cards.views.search_by_country', name='list-by-country'),
	url(r'^list/category/(?P<category_id>\d+)/$', 'cards.views.search_by_category', name='list-by-category'),
	url(r'^list/subcategory/(?P<subcategory_id>\d+)/$', 'cards.views.search_by_subcategory', name='list-by-subcategory'),
	url(r'^list/tag/(?P<tag_id>\d+)/$', 'cards.views.search_by_tag', name='list-by-tag'),
	url(r'^charts/$', 'cards.views.charts', name='charts'),
	url(r'^map/$', 'osm.views.map', name='map'),
	
	
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),	
	url(r'^$', 'cards.views.index', name='index'),
)

urlpatterns += staticfiles_urlpatterns()
