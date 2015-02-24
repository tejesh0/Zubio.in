from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from users_zubio.views import seller_form,buyer_feed
import allauth.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zubio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sell/', seller_form),
    url(r'$', buyer_feed),
    url(r'^accounts/', include(allauth.urls)),
    url(r'^messages/', include('postman.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )