from django.shortcuts import render
from .models import Note
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
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

class NoteListView(ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    ordering = ['-created_at']

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'notes'

class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    fields = ['title','body']
    template_name = "notes/note_form.html"
    success_url = reverse_lazy('notes-home')

    def form_valid(self,form):
        print("Formulario válido recibido")
        form.instance.author = self.request.user
        return super().form_valid(form)
