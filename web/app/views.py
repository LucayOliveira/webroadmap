from django.shortcuts import render

# Create your views here.

def Homepage(request):
  return render(request, 'homepage.html')

def Loja(request):
  return render(request, 'loja.html')

def Login(request):
  return render(request, 'login.html')

def Minhaconta(request):
  return render(request, 'minhaconta.html')

def Carrinho(request):
  return render(request, 'carrinho.html')
