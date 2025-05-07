from django.urls import path, include 
from .views import *

urlpatterns = [
    path('', Homepage, name='Homepage'),
    path('loja/', Loja, name='Loja'),
    path('login/', Login, name='Login'),
    path('minhaconta/', Minhaconta, name='Minhaconta'),
    path('carrinho/', Carrinho, name='carrinho'),
]