from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import settings


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('strona.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
