from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.models import User

from accounts.forms import RegisterForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'auth/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_path = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next_path:
                return HttpResponseRedirect(next_path)
            
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, 'auth/login.html', {'has_error': True})


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)


class RegisterView(CreateView):
    model = User
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("webapp:courses_list")
