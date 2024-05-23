from django.urls import path
from .views import get_insights, get_investimento, get_comparativo

urlpatterns = [
    path('get_insights/', get_insights, name='get_insights'),
    path('get_investimento/', get_investimento, name='get_investimento'),
    path('get_comparativo/', get_comparativo, name='get_comparativo')
]
