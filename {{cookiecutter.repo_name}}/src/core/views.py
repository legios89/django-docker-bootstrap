# coding: utf-8
# Core and 3th party packages
{% if cookiecutter.use_react == 'True' -%}
from rest_framework.views import APIView
from rest_framework.response import Response
{% if cookiecutter.use_translation != 'True' -%}
from django.core.urlresolvers import reverse
{% endif -%}
{% endif -%}
{% if cookiecutter.use_translation == 'True' -%}
from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class PublishRosetta(View):
    def get(self, request):
        try:
            import uwsgi
            uwsgi.reload()
        except ImportError:
            pass  # Probably the django started with runserver
        return HttpResponseRedirect(reverse('rosetta-home'))
{% else -%}
from django.views.generic import TemplateView
{% endif %}

class HomePageView(TemplateView):
    template_name = "home.html"
{% if cookiecutter.use_react == 'True' %}

class UrlsApi(APIView):
    def get(self, request, format=None):
        return Response({'admin_index': reverse('admin:index')})
{%- endif %}
