from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from . import views
from gestionVente.views import recherche_produit as recherche_produit
from django.contrib import admin


app_name='gestionProduit'

urlpatterns = [
    path('', views.menu,name='menu'),
    path('gestion_produits', views.gestion_produits,name='produit'),
    path('affichageProduit', views.affichageProduit, name='affichage_produit'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('page1', views.page1, name='page1'), 
    path('formulaireCategorie', views.formulaireCategorie, name='formulaireCategorie'), 
    path('afficher_categories', views.afficher_categories, name='afficher_categories'),
    path('supprimer_categorie/<int:categorie_id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('recherche_produit', views.recherche_produit, name='recherche_produit'), 
    path('transactions', views.transactions, name='transactions'),
    path('validation', views.validation, name='validation'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('<int:id>/', views.ajouter_panier, name='ajouter_panier'),
    path('afficher_panier/', views.afficher_panier, name='afficher_panier'),
    path('deletePanier/', views.deletePanier, name='deletePanier'),
    path('recu/<int:transaction_id>', views.recu, name='recu'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('statistiques_json', views.statistiques_json, name='statistiques_json'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
