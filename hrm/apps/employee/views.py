from django.shortcuts import render
from django.contrib.auth.views import LoginView

from django.views.generic.base import TemplateView


class IdentifyUserView(TemplateView):
    template_name = "identify-user.html"

# Create your views here.
