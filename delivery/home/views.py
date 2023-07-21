from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .form import add_car
from django.http import JsonResponse
# Create your views here.

def catalogo(request):

    return render(request, 'home/template/card-2.html', {
        'form':add_car()
    })

def catalogo_1(request):

    return render(request, 'home/template/index.html')

def objcar(request):
    obj = request.POST
    print(obj)
    return JsonResponse({'price':obj['catidad']})

def create_item(request):
    obj = request.POST
    print(obj)

    return render(request, 'home/template/create.html')
