from django.shortcuts import render
from api.models import Note
from django.http import HttpResponse

notes = [
    {
        "title": "Una nota",
        "body": "Esto es una nota"
    },
    {
        "title": "Otra nota",
        "body": "Esto es otra nota"
    }

]

def home(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request,'notes/home.html',context)


def about(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request,'notes/home.html',context)
