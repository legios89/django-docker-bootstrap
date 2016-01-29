# coding: utf-8
# Core and 3th party packages
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
{% if cookiecutter.use_translation == 'True' -%}
from django.conf.urls.i18n import i18n_patterns

# Project imports
from .views import PublishRosetta
{% endif %}

{% if cookiecutter.use_translation == 'True' -%}
urlpatterns = i18n_patterns(
{%- else -%}
urlpatterns = [
{%- endif %}
    url(r'^admin/', include(admin.site.urls)),
{%- if cookiecutter.use_translation == 'True' %}
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^publish/rosetta/', PublishRosetta.as_view(), name='publish_rosetta')
)
{% else %}
]
{% endif %}
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
