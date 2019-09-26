from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, resolve_url, redirect
from django.urls import reverse
from django.views import View

from nucleo.forms import LoginForm


class ClienteLogin(LoginView):

    def is_valid_user(self):
        a = ''
        return hasattr(self.request.user,
                       'is_staff') and self.request.user.is_staff and self.request.user.is_active and not self.request.user.is_block

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('nucleo:inicio')


class LoginView(ClienteLogin):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('nucleo:inicio')


class InicioViewSet(View):

    def get(self, request):
        usuario = request.user
        if usuario.is_anonymous:
            return redirect(reverse('nucleo:login'))
        return render(request, 'inicio.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('nucleo:login'))
