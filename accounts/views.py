from django.shortcuts import render
from django.contrib.auth import (authenticate, login, logout, update_session_auth_hash)
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import *

# Create your views here.

def cadastrar_usuario(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request,'Olá ' + username + '! A sua conta criada com sucesso')
            return HttpResponseRedirect(reverse('accounts:user-login'))
    context = {'form':form}
    return render(request, 'accounts/signupPage.html',context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        usuario = User.objects.filter(username = str(username))
        password = request.POST.get('password')
        if usuario.exists():
            user = authenticate(request, username = username , password = password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Login feito')
                return HttpResponseRedirect(reverse('accounts:sucesso'))
            else:
                messages.warning(request, 'Palavra-passe incorreta')
                return render(request, 'accounts/index.html')
        else:
            messages.warning(request, 'Usuário não existe ou campos vazios')
            return render(request, 'accounts/index.html')
    context = {}
    return render(request, 'accounts/index.html',context)

def sucesso(request):
    return render(request, 'accounts/sucesso.html')

def logout_user(request):
    logout(request)
    return user_login(request)