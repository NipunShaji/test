
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url

from apps.hr.forms import HrAuthenticationForm



class HRLoginView(LoginView):

    form_class = HrAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True
    redirect_url = "/hr/employees/"

    def get_default_redirect_url(self):
        return resolve_url(self.redirect_url)
