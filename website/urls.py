from django.conf.urls.defaults import *
from django.views.generic import TemplateView

import views


urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', TemplateView.as_view(template_name="index_en.html")),
)
