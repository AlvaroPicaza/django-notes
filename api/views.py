from django.shortcuts import render
from .models import Note
def home(request):
    context = {
        'note': Note.objects.all()
    }
    return render(request,'',context)