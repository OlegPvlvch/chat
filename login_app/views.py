
from django.contrib.auth import views, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render, redirect


class MyLoginView(views.LoginView):
    template_name = 'login_app/login.html'

class SignUpView(View):
    form_class = UserCreationForm
    template_name = 'login_app/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            u_name = form.cleaned_data.get('username')
            u_pass = form.cleaned_data.get('password1')
            user = authenticate(username=u_name, password=u_pass)
            login(request, user)
            return redirect('index')
        return render(request, self.template_name, {'form':form})