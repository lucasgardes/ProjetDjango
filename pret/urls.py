from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emprunt/create/<int:materiel_id>/', views.emprunt_create, name='emprunt_create'),
    path('emprunts/', views.emprunt_list, name='emprunt_list'),
    path('emprunt/return/<int:emprunt_id>/', views.emprunt_return, name='emprunt_return'),
    path('emprunt/history/<int:materiel_id>/', views.emprunt_history, name='emprunt_history'),
    path('add/enseignant/', views.add_enseignant, name='add_enseignant'),
    path('add/materiel/', views.add_materiel, name='add_materiel'),
    path('add/accessoire/', views.add_accessoire, name='add_accessoire'),
    path('budget/list/', views.budget_list, name='budget_list'),
    path('salle/materiel/<int:materiel_id>/', views.salle_materiel, name='salle_materiel'),
    path('materiels/responsable/<int:responsable_id>/', views.materiels_responsable, name='materiels_responsable'),
    path('responsables/', views.liste_responsables, name='liste_responsables'),
    path('historique/materiel/<int:materiel_id>/', views.historique_materiel, name='historique_materiel'),
    path('salles/', views.liste_salles, name='liste_salles'),
    path('salles/<int:salle_id>/', views.materiels_salle, name='materiels_salle'),
    path('materiels/', views.liste_materiels, name='liste_materiels'),
    path('materiels/<int:materiel_id>/', views.details_materiel, name='details_materiel'),
    path('emprunts/materiel/<int:materiel_id>/', views.emprunts_materiel, name='emprunts_materiel'),
    path('gestion_pret/', views.gestion_pret, name='gestion_pret'),
]