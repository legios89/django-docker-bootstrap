# coding: utf-8
# Core and 3th party packages
from django.views.generic import View
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
