from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

def unautenticate_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('morador:indexMorador'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Não está autorizado')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
         group = None
         if request.user.groups.exists():
             group = request.user.groups.all()[0].name
         if group == 'morador':
             return view_func(request, *args, **kwargs)

         if group == 'funcionario':
             return HttpResponseRedirect(reverse('funcionario:index'))

         if group == 'portaria':
            return HttpResponseRedirect(reverse('portatia:indexPortaria'))

         if group == 'admin':
           return HttpResponseRedirect(reverse('gestaoCondominio:index'))
    return wrapper_function
