from django.urls import path
from .views import ativos, salvar, editar, update, delete, plataforma
from . import views

urlpatterns = [
    path('', ativos, name='ativos'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('erro/', views.erro, name='erro'),
    path('erro_ativo/', views.erro_ativo, name='erro_ativo'),
]