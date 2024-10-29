from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

app_name='gestionVente'

urlpatterns = [
    path('', views.recherche_produit, name='recherche_produit'),
]


