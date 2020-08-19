from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404


class HomePage(TemplateView):
    template_name='blog/home.html'
    allowed_site = ['localhost', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.site.domain not in self.allowed_site:
            raise Http404("Not allowed")
        context['site_name'] = self.request.site.name
        return context
