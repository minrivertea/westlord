from django.conf.urls.defaults import *
from django.conf import settings
from website.models import *
from django.contrib.sitemaps import GenericSitemap
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^', include('website.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
    url(r'^zh/', TemplateView.as_view(template_name="index_zh.html")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


