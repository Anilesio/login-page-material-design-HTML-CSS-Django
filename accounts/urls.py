from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from .views import *

app_name= 'accounts'
urlpatterns = [
    url(r'^$', user_login, name='user-login'),
    url(r'^logout-user$', logout_user, name='logout-user'),
    url(r'^cadastrar-usuario$', cadastrar_usuario, name='cadastrar-usuario'),
    url(r'^sucesso$', sucesso, name='sucesso'),
]