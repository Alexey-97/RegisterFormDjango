from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import  redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import UserData
from .forms import RegisterForm 
from django.contrib.auth.models import User



# Create your views here.
def registration(request):
    """регистрация и аунтификация"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserData.objects.create(user=user, phone=form.cleaned_data.get('phone'))
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return render(request,"user_auth/home_page.html",{})
        else:
            print('ОШИБКА: ', form.errors.as_text())
            return render(request,"user_auth/error404.html",{})
    else:
        form = RegisterForm()
        return render(request, 'user_auth/sign_up.html', {'form': form})



class LoginUser(LoginView):
    "Авторизация пользователя"
    form_class = AuthenticationForm
    template_name = 'user_auth/sign_in.html'



def home(request):
    return HttpResponse("<h1>Вы успешно Авторизовались</h1>")

