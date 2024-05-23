from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .utils import get_or_create_guest_user
from django.utils import timezone
from datetime import datetime, timedelta
from .models import UserProfile
from datetime import date
import requests

def cadastro_fail(request):
    return render(request, 'cadastro_fail.html')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        
        if user:
            return redirect('cadastro_fail')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect('plataforma')       
    
def login_fail(request):
    return render(request, 'login_fail.html')

def api_request(tipo, codigo):
    response = requests.get(f'http://127.0.0.1:8000/{tipo}/{codigo}')
    if response.status_code == 200:
        return response.json()
    else:
        return None
def update_data(user):
    now = timezone.now()
    profile, created = UserProfile.objects.get_or_create(user=user)
    if created or now - profile.last_update > timedelta(days=1):
        for ativo in user.ativos.all():
            data = api_request(ativo.tipo, ativo.codigo)

            today = date.today()
            date_key = today.strftime("%d/%m/%Y")
            if data is not None:
                data_ativo = data[date_key][ativo.codigo]

                ativo.cotacao = data_ativo.get('Cotação', 0.0) 
                ativo.dividend_yield = data_ativo.get('Dividend Yield', '-')
                ativo.p_vp = data_ativo.get('P/VP', '-')
                ativo.liquidez_diaria = data_ativo.get('Liquidez Diária', '-')
                ativo.p_l = data_ativo.get('P/L', '-')
                ativo.variacao_24h = data_ativo.get('Variação (24h)', '-')
                ativo.variacao_12m = data_ativo.get('Variação (12M)', '-')
                ativo.variacao_24m = data_ativo.get('Variação (24M)', '-')
                ativo.variacao_60m = data_ativo.get('Variação (60M)', '-')

                ativo.save()

        profile.last_update = now
        profile.save()

def cleanup_guest_users():
    one_day_ago = timezone.now() - timezone.timedelta(days=1)
    all_users = UserProfile.objects.all()
    print(f"All users: {[user.user.username for user in all_users]}")
    print(f"Last active: {[user.last_active for user in all_users]}")

    users_to_delete = UserProfile.objects.filter(user__username__startswith='convidado_finz_n', last_active__lt=one_day_ago)
    print(f"Deleting {users_to_delete.count()} users")

    for user_profile in users_to_delete:
        try:
            user_profile.user.delete()
            print(f"Deleted {users_to_delete.count()} users")
        except Exception as e:
            print(f"Error deleting user {user_profile.user.username}: {e}")


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username_or_email = request.POST.get('username')
        senha = request.POST.get('senha')

        User = get_user_model()

        user = User.objects.filter(username=username_or_email).first()
        if not user:
            user = User.objects.filter(email=username_or_email).first()

        if user and user.check_password(senha):
            login_django(request, user)
            update_data(user) 
            cleanup_guest_users()
            return redirect('plataforma')
        else:
            return redirect('login_fail')

def guest_login(request):
    guest_user = get_or_create_guest_user(request)
    return JsonResponse({'username': guest_user.user.username})


def home(request):
    return render(request, 'home.html')

def logout(request):
    auth_logout(request)
    return redirect('home')




