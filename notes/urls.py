"""
URL configuration for notable_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from api.resources import NoteResource
from . import views

#note_resource = NoteResource()

urlpatterns = [
    path('', views.NoteListView.as_view(), name='notes-home'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('new/', views.NoteCreateView.as_view(), name='note-create'),
    #path('api/', include(note_resource.urls)),
    path('about/', views.about, name='notes-about'),
    
]
