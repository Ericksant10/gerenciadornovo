from django import forms
from .models import Materia, Topico

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nome']

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['nome', 'materia']
