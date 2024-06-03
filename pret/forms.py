from django import forms
from .models import Emprunt, Enseignant, Materiel, Accessoire, HistoriquePassation

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['possesseur', 'commentaires']
        
class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom']

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['nom', 'responsable', 'salle_actuelle', 'budget', 'montant', 'accessoires']
        accessoires = forms.ModelMultipleChoiceField(queryset=Accessoire.objects.all(), widget=forms.CheckboxSelectMultiple)
        
class AccessoireForm(forms.ModelForm):
    class Meta:
        model = Accessoire
        fields = ['nom', 'etat']

class HistoriquePassationForm(forms.ModelForm):
    class Meta:
        model = HistoriquePassation
        fields = ['lieu', 'occasion', 'objectif_utilisation', 'etat_accessoires']
