from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    datas = [{'deal': 'Sale',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT48oA-vbvdUT0mDK_PS3xvUGhq9sIiSAVobw&usqp=CAU',
            'cash_back': 'buy 3 and get 1 free'},
            {'deal': 'Время для шоппинга',
             'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZGBEZZOQVp2G2TErRAsz-rzuLCBbINoNVvA&usqp=CAU',
             'cash_back': 'Купи 2 по цене одной'},
            {'deal': 'Wildberries',
             'img': 'https://aslabunova.com/wp-content/uploads/2017/08/000012432632.jpg?w=2000',
             'cash_back': 'Дешевле чем на Wildberries'},
            {'deal': 'Детский шопинг',
             'img': 'https://workingmama.ru/wp-content/uploads/2020/11/dsc6789_retouch-720x480.jpg',
             'cash_back': 'Our children'},
            {'deal': 'Шопинг, шопинг, шопинг',
             'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwXHjfedXZsTOL5vFUfkPb-herjcAyHy0ZUA&usqp=CAU',
             'cash_back': 'горячие скидки'},
            {'deal': 'For all',
             'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaNkuTm6hFYsJPYsRqcFt733a08-oMsCshRQ&usqp=CAU',
             'cash_back': 'Шопинг для всех'},

            ]

    return render(request, 'main.html', {'data': datas})




def my_list(request):
    return HttpResponse("my_list`s list")

def about_us(request):
    return HttpResponse("consulting for people")

def contucts(request):
    return HttpResponse("adress and contacts")

def prices(request):
    return HttpResponse("Our price")

def teacher(request):
    return HttpResponse("Our teachers")

def leadership(request):
    return HttpResponse("Leadership")

def profiles(request):
    return HttpResponse("Our profiles in SM")

def achievements(request):
    return HttpResponse("achievements of our students")

def vacancies(request):
    return HttpResponse("Vacancies in academy")


