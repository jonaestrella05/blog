from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'core/home.html')


def portafolio(request):
    return render(request, 'core/portafolio.html')


def contacto(request):
    return render(request, 'core/contacto.html')


def cv(request):
    return render(request, 'core/cv.html')

# Create your views here.
