from django.shortcuts import render
from django.http import HttpResponse

from .models import Author

# Create your views here.
def index(request):
    return HttpResponse("HOLA MUNDO.")

def listarAutores(request):
    lista = Author.objects.all()
    output = ', '.join([a.first_name for a in lista])
    return HttpResponse(output)
