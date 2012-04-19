from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from links.api import LinkResource,TagResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(LinkResource())
v1_api.register(TagResource())



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lasso.views.home', name='home'),
    # url(r'^lasso/', include('lasso.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^api/', include(v1_api.urls)),
)
