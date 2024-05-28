from django import forms
from .models import Emprunt

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['possesseur', 'commentaires']
