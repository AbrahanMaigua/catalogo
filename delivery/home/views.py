from django.shortcuts import render

# Create your views here.

def catalogo(request):

    return render(request, 'home/template/card-2.html')

def catalogo_1(request):

    return render(request, 'home/template/index.html')