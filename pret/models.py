from django.db import models
from django.utils import timezone

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Salle(models.Model):
    numero = models.CharField(max_length=10)
    
    def __str__(self):
        return self.numero

class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    responsable = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='materiels')
    salle_actuelle = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True, related_name='materiels')
    
    def __str__(self):
        return self.nom
    
class Emprunt(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, related_name='emprunts')
    possesseur = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='emprunts')
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour = models.DateTimeField(null=True, blank=True)
    commentaires = models.TextField(blank=True)

    def __str__(self):
        return f"{self.materiel.nom} emprunté par {self.possesseur.nom}"
