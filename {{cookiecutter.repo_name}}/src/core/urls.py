# coding: utf-8
# Core and 3th party packages
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    {% if cookiecutter.use_rosetta == 'True' -%}
    url(r'^rosetta/', include('rosetta.urls')),
    {%- endif %}
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
