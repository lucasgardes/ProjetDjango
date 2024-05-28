from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emprunt/create/<int:materiel_id>/', views.emprunt_create, name='emprunt_create'),
    path('emprunts/', views.emprunt_list, name='emprunt_list'),
]