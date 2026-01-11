from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

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

#NoteListCreateView, filtra por usuario loggeado

class UserNoteListCreateView(LoginRequiredMixin, FormMixin, ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    ordering = ['-created_at']
    form_class = NoteForm
    success_url = reverse_lazy('notes-home')

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)   
    
    def get_queryset(self):
        return Note.objects.filter(author=User.objects.filter(username=self.request.user.username)[0]).order_by("-created_at")

#NoteListCreateView, NO filtra por usuario loggeado

class NoteListCreateView(LoginRequiredMixin, FormMixin, ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    ordering = ['-created_at']
    form_class = NoteForm
    success_url = reverse_lazy('notes-home')

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)   

"""class NoteListView(ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    ordering = ['-created_at']"""


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'notes'
    ordering = ['-created_at']
    form_class = NoteForm
    success_url = reverse_lazy('notes-home')



class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    fields = ['title','body']
    template_name = "notes/home.html"
    success_url = reverse_lazy('notes-home')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model = Note
    fields = ['title','body']
    template_name = "notes/note_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #obtenemos el post que estamos actualizando y comprobamos que su autor sea el mismo usuario que esta logeado
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        
        return False
    
class NoteDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Note
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
    
        return False