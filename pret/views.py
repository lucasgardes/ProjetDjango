from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Materiel, Enseignant, Emprunt, Accessoire, HistoriquePassation, Salle
from .forms import EmpruntForm, EnseignantForm, MaterielForm, AccessoireForm, HistoriquePassationForm

def index(request):
    materiels = Materiel.objects.all()
    return render(request, 'pret/index.html', {'materiels': materiels})

def gestion_pret(request):
    return render(request, 'pret/gestion_pret.html')

def emprunt_create(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    possesseur_precedent = materiel.possesseur_actuel
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        historique_form = HistoriquePassationForm(request.POST)
        if form.is_valid() and historique_form.is_valid():
            emprunt = form.save(commit=False)
            emprunt.materiel = materiel
            emprunt.date_emprunt = timezone.now()
            emprunt.save()
            
            materiel.possesseur_actuel = emprunt.possesseur
            materiel.save()
            
            historique_passation = HistoriquePassation.objects.create(
                materiel=materiel,
                possesseur_precedent=possesseur_precedent,
                possesseur_actuel=emprunt.possesseur,
                date_passation=timezone.now(),
                lieu=historique_form.cleaned_data['lieu'],
                objectif_utilisation=historique_form.cleaned_data['objectif_utilisation'],
            )
            historique_passation.accessoires.set(materiel.accessoires.all())
            form.save_m2m()
            return redirect('emprunt_list')
    else:
        form = EmpruntForm()
        historique_form = HistoriquePassationForm()
    return render(request, 'pret/emprunt_form.html', {'form': form, 'historique_form': historique_form, 'materiel': materiel})

def emprunt_list(request):
    emprunts = Emprunt.objects.all().select_related('materiel', 'possesseur')
    return render(request, 'pret/emprunt_list.html', {'emprunts': emprunts})

def emprunt_return(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)
    emprunt.retourner()
    emprunt.materiel.possesseur_actuel = emprunt.materiel.responsable
    emprunt.materiel.save()
    return redirect('emprunt_list')

def emprunt_history(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    emprunts = materiel.emprunts.all()
    return render(request, 'pret/emprunt_history.html', {'materiel': materiel, 'emprunts': emprunts})

def add_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EnseignantForm()
    return render(request, 'pret/add_enseignant.html', {'form': form})

def add_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MaterielForm()
    return render(request, 'pret/add_materiel.html', {'form': form})

def budget_list(request):
    materiels = Materiel.objects.all()
    return render(request, 'pret/budget_list.html', {'materiels': materiels})

def add_accessoire(request):
    if request.method == 'POST':
        form = AccessoireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AccessoireForm()
    return render(request, 'pret/add_accessoire.html', {'form': form})

def salle_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    return render(request, 'pret/salle_materiel.html', {'materiel': materiel})

def materiels_responsable(request, responsable_id):
    responsable = get_object_or_404(Enseignant, id=responsable_id)
    materiels = Materiel.objects.filter(responsable=responsable)
    return render(request, 'pret/materiels_responsable.html', {'responsable': responsable, 'materiels': materiels})

def historique_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    historiques = materiel.historiques.all()
    return render(request, 'pret/historique_materiel.html', {'materiel': materiel, 'historiques': historiques})

def liste_responsables(request):
    responsables = Enseignant.objects.all()
    return render(request, 'pret/liste_responsables.html', {'responsables': responsables})

def liste_salles(request):
    salles = Salle.objects.all()
    return render(request, 'pret/liste_salles.html', {'salles': salles})

def materiels_salle(request, salle_id):
    salle = get_object_or_404(Salle, id=salle_id)
    materiels = Materiel.objects.filter(salle_actuelle=salle)
    return render(request, 'pret/materiels_salle.html', {'salle': salle, 'materiels': materiels})

def liste_materiels(request):
    materiels = Materiel.objects.all()
    return render(request, 'pret/liste_materiels.html', {'materiels': materiels})

def details_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    return render(request, 'pret/details_materiel.html', {'materiel': materiel})

def emprunts_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    emprunts = Emprunt.objects.filter(materiel=materiel)
    return render(request, 'pret/emprunts_materiel.html', {'materiel': materiel, 'emprunts': emprunts})