from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm



class RegisterView(CreateView):
    template_name='register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('login')


class LoginView(View):
    template_name='login.html'
    form_class=LoginForm


    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    
    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create_short_url')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('create_short_url')
