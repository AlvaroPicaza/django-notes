from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm

def register(request):
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                 username = form.cleaned_data.get("username")
                 messages.success(request = request,message=f"Usuario {username} creado correctamente. Ya puedes acceder")
                 form.save()
                 return redirect('login')

        else: 
            form = UserRegisterForm()
        return render(request,'users/register.html',{'form':form})

"""def login(request):
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                 username = form.cleaned_data.get("username")
                 messages.success(request = request,message=f"Usuario {username} creado correctamente")
                 form.save()
                 return redirect('notes-home')

        else: 
            form = UserRegisterForm()
        return render(request,'users/register.html',{'form':form})"""

class CustomLoginView(LoginView):
    authentication_form  = UserLoginForm
    template_name = "users/login.html"

    def post(self, request, *args, **kwargs):
        print("POST RECIBIDO")
        return super().post(request, *args, **kwargs)