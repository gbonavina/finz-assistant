from django.contrib import admin
from django.urls import path, include
from  usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('core/', include('core.urls')),
    path('', views.home, name='home'),
    path('api_gemini/', include('api_gemini.urls')),
    path('logout/', views.logout, name='logout'),
]

