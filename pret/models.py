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
    
class Accessoire(models.Model):
    nom = models.CharField(max_length=100)
    etat = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.nom

class Materiel(models.Model):
    BUDGET_CHOICES = [
        ('annee_courante', 'Budget de l\'année courante'),
        ('projet', 'Budget projets'),
        ('exceptionnel', 'Budget financements exceptionnels'),
    ]
    
    nom = models.CharField(max_length=100)
    responsable = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='materiels')
    salle_actuelle = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True, related_name='materiels')
    possesseur_actuel = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='materiel_possede', blank=True)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, default='annee_courante')
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    accessoires = models.ManyToManyField(Accessoire, blank=True)

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
    
    def retourner(self):
        self.date_retour = timezone.now()
        self.save()

class HistoriquePassation(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, related_name='historiques')
    possesseur_precedent = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='precedent_historiques')
    possesseur_actuel = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='actuel_historiques')
    date_passation = models.DateTimeField(default=timezone.now)
    lieu = models.CharField(max_length=100, blank=True)
    occasion = models.CharField(max_length=100, blank=True)
    objectif_utilisation = models.TextField(blank=True)
    accessoires = models.ManyToManyField(Accessoire, blank=True)
    etat_accessoires = models.TextField(blank=True)

    def __str__(self):
        return f"Passation de {self.possesseur_precedent} à {self.possesseur_actuel} pour {self.materiel.nom}"