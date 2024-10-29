from django.shortcuts import render
from gestionProduit.models import *

def recherche_produit(request):
    terme_recherche = request.GET.get('terme_recherche', '')

    if terme_recherche:
        # Effectuez la recherche dans la base de données
        resultats = Produit.objects.filter(nom_produit__icontains=terme_recherche)
    else:
        resultats = None

    return render(request, 'rechercheProduit.html', {'resultats': resultats, 'terme_recherche': terme_recherche})
