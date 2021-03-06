from SpouseChoices import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KitchenPassWebApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='Spouse_list'),
    url(r'^(?P<SpouseRequest_id>\d+)/$', views.detail, name='detail'),
    url(r'^message/(?P<SpouseRequest_id>\d+)/device/(?P<Device_id>\d+)/$', views.sendPost, name='sendPost'),
    url(r'', include('gcm.urls')),
)
