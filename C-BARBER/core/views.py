from django.shortcuts import render, HttpResponse

def inicio(request):
    return render(request, "core/index.html")

def agendar(request):
    return render(request, "core/agendar.html")

def contac(request):
    return render(request, "core/contactame.html")

def galeria(request):
    return render(request, "core/galeria.html")

def inf(request):
    return render(request, "core/info.html")


    