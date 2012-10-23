from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import views


urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'index_en.html',}),
)

urlpatterns += patterns('',
    url(r'^update/$', views.userEdit, name="useredit"),
)
