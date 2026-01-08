from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserLoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid():
             username = request.user.username
             u_form.save()
             p_form.save()
             messages.success(request=request,message=f"Se ha modificado el perfil de {username}")
             return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    request.user.profile
                                    )

        context={
            'u_form':u_form,
            'p_form':p_form
        }

        return render(request,'users/profile.html',context)
        
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