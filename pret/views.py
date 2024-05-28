from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Materiel, Enseignant, Emprunt
from .forms import EmpruntForm

def index(request):
    materiels = Materiel.objects.all()
    return render(request, 'pret/index.html', {'materiels': materiels})

def emprunt_create(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)
            emprunt.materiel = materiel
            emprunt.date_emprunt = timezone.now()
            emprunt.save()
            return redirect('index')
    else:
        form = EmpruntForm()
    return render(request, 'pret/emprunt_form.html', {'form': form, 'materiel': materiel})

def emprunt_list(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'pret/emprunt_list.html', {'emprunts': emprunts})
