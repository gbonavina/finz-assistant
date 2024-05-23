from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/fail/', views.cadastro_fail, name='cadastro_fail'),
    path('login/', views.login, name='login'),
    path('login/fail/', views.login_fail, name='login_fail'),
    path('logout/', views.logout, name='logout'),
    path('guest_login/', views.guest_login, name='guest_login'),
]