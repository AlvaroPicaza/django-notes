from django.shortcuts import render, redirect
from django.contrib import messages
#from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def register(request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                 username = form.cleaned_data.get("username")
                 messages.success(request = request,message=f"Usuario {username} creado correctamente")
                 return redirect('notes-home')

        else: 
            form = UserCreationForm()
        return render(request,'users/register.html',{'form':form})