from django.conf.urls import patterns, include, url
from django.contrib import admin
import gym.urls
import gym.views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zubio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', gym.views.index),
    url(r'^list/', gym.views.list),
    url(r'^login/', gym.views.login),
    url(r'^gymprofile/', gym.views.gym_profile),
    url(r'^index/', gym.views.index),

    


)

