from django import forms
from .models import Note

class NoteForm(forms.ModelForm):

    title = forms.CharField(label="Título",
                            widget=forms.TextInput(attrs={"class":"form-control",
                                                          "placeholder":"Título"})
                            )

    body = forms.CharField(label="Contenido",
                           widget=forms.TextInput(attrs={"class":"form-control",
                                                          "placeholder":"Contenido"})
                           )

    class Meta:
        model = Note
        fields = ['title', 'body']
