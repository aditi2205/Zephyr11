from django.shortcuts import render


from django.http import HttpResponse
from django.template import Context, loader

def DashBoard(request):
    return render(request, 'dashboard.html')

def LOC(request):
    return render(request, 'LOCPage.html')


def Offers(request):
    return render(request, 'offers.html')

def ChatBot(request):
    return render(request, 'chatbot.html')

def service_all(request):
    posts = Service.objects.all()
    print (posts)
    return render(request, "list.html", {'posts': posts})