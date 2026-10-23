from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404

from django.conf import settings
from .models import Profile, Hobbie, Project
from django.views.generic import TemplateView
from django.utils import translation

# Create your views here.

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language) 
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
    else:
        response = HttpResponseRedirect('/')
    return response


class indexView(TemplateView):
    model = Profile
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(id=1)
        return context
    


# def index(request):
#     profile = Profile.objects
#     return render(request, 'index.html')