from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):

    return render(request,"index.html")

def registrousuario(request):

    return render(request,"registrousuario.html")
def menuforo(request):

    return render(request,"menuforo2.html")

def buscar(request):
    
    mensaje="Articulo: %r" %request.GET["username"]

    return HttpResponse(mensaje)