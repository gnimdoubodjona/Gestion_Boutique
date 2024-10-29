from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import *
from gestionVente.views import recherche_produit as recherche_produit
from django.template.loader import get_template
from django.shortcuts import render
from xhtml2pdf import pisa
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Sum

recherche_produit = recherche_produit


def menu(request):
    produits = Produit.objects.select_related('categorie').all()
    nouveaux_produits = Produit.objects.order_by('-creer_a')[:8]
    categories = Categorie.objects.all()

    context = {
        "produits": produits,
        "nouveaux_produits_data": zip(nouveaux_produits, categories),
        "produit": produits.first(),
    }

    return render(request, 'menu.html', context=context)


def gestion_produits(request):
    categories = Categorie.objects.all()
    if request.method == 'POST':
        categorie_id = request.POST.get('nom_categorie')
        nom_produit = request.POST.get('nom_produit')
        quantite_produit = request.POST.get('quantite_produit')
        prix = request.POST.get('prix')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        est_vendu = request.FILES.get('est_vendu')
        creer_a = request.FILES.get('creer_a')

        cat = get_object_or_404(Categorie, pk=categorie_id)

        nouveau_produit = Produit.objects.create(
            nom_produit=nom_produit,
            quantite_produit=quantite_produit,
            prix=prix,
            categorie=cat,
            image=image,
            est_vendu=est_vendu,
            creer_a=creer_a,
            description=description
        )

        return redirect('/affichageProduit')

    return render(request, 'page1.html', {'categories': categories})



def formulaireCategorie(request):
    if request.method == 'POST':
        nom_categorie = request.POST.get('nom_categorie')
        categorie_existante = Categorie.objects.filter(nom_categorie=nom_categorie).first()
        if not categorie_existante:
            nouvelle_categorie = Categorie.objects.create(nom_categorie=nom_categorie)
            return redirect('gestionProduit:afficher_categories')
    return render(request, 'formulaireCategorie.html')



def afficher_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'afficherCategorie.html', {'categories': categories})
#return render(request, 'afficherCategorie.html', {'categories': categories})


def supprimer_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    if request.method == 'POST':
        # Confirmation de la suppression (si nécessaire)
        confirmation = request.POST.get('confirmation', '')

        if confirmation.lower() == 'oui':
            # Supprimer la catégorie et ses produits associés
            categorie.produit_set.all().delete()
            categorie.delete()

            return redirect('/afficher_categories')

    return render(request, 'supprimerCategorie.html', {'categorie': categorie})
    
def affichageProduit(request):
    produits = Produit.objects.all()
    return render(request, 'affichageProduit.html', {'produits': produits})


def delete(request, id):
    produit = Produit.objects.get(id=id)
    produit.delete()
    return redirect("/affichageProduit")


# def update(request, id):
#     if request.method == 'POST':
#         produit_mis_a_jour = request.POST.get('nom_produit')
#         quantite_produit_mis_a_jour = request.POST.get('quantite_produit')
#         prix_mis_a_jour = request.POST.get('prix')
#         nom_categorie_mis_a_jour = request.POST.get('nom_categorie')

#         # Rechercher une catégorie existante ou créer une nouvelle
#         nouvelle_categorie, created = Categorie.objects.get_or_create(nom_categorie=nom_categorie_mis_a_jour)

#         # Mettre à jour le produit existant ou créer un nouveau
#         produit = Produit.objects.get(id=id)
#         produit.nom_produit = produit_mis_a_jour
#         produit.quantite_produit = quantite_produit_mis_a_jour
#         produit.prix = prix_mis_a_jour
#         produit.categorie = nouvelle_categorie
#         produit.save()

#         return redirect('/affichageProduit')
    


def update(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        produit_mis_a_jour = request.POST.get('nom_produit')
        quantite_produit_mis_a_jour = request.POST.get('quantite_produit')
        prix_mis_a_jour = request.POST.get('prix')
#        nom_categorie_mis_a_jour = request.POST.get('nom_categorie')
        # Votre code de mise à jour ici...
        return redirect('/affichageProduit')
    
    categories = Categorie.objects.all()
    context = {
        'produit': produit,
        'categories': categories,
    }
    return render(request, 'miseAJour.html', context)

def page1(request):
    categories = Categorie.objects.all()
    return render(request, 'page1.html', {'categories': categories})

def detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    related_items = Produit.objects.filter(categorie=produit.categorie).exclude(pk=pk)[0:5]

    return render(request, 'detail.html', {
        'produit': produit,
        'related_items': related_items
    })
    

def ajouter_panier(request, id):
    produit = get_object_or_404(Produit, id=id)
    panier, _ = Panier.objects.get_or_create(user=request.user)
    produit_panier, created = produitPanier.objects.get_or_create(panierAssocier=panier, produitAssocier=produit)
    # Si le produit n'est pas encore dans le panier
    if created:
        panier.produits.add(produit)
        panier.save()
    else:
        produit_panier.quantite_produit += 1
        produit_panier.save()
    
    return redirect('gestionProduit:detail', pk=id)


def afficher_panier(request):
    produit_paniers = produitPanier.objects.filter(user=request.user)
    produitAssocier=produitPanier.objects.all()
    nombre_articles_panier = produit_paniers.count()
    return render(request, 'ajouterPanier.html', {'produit_paniers': produit_paniers, 'produitAssocier':produitAssocier,'nombre_articles_panier': nombre_articles_panier})

def recu(request,transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    # Charger le template du reçu/facture
    template_path = 'recu.html'
    context = {'transaction': transaction}
    template = get_template(template_path)
    html = template.render(context)
    # Créer un fichier PDF à partir du HTML généré
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=receipt_{transaction_id}.pdf'
    pisa_status = pisa.CreatePDF(html, dest=response)
    # Vérifier si la génération du PDF a réussi
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du reçu/facture', content_type='text/plain')
    return response

def transactions(request):
    panier_utilisateur = Panier.objects.get(user=request.user)
    # Créer une nouvelle transaction sans utiliser la relation OneToOneField
    nouvelle_transaction = Transaction.objects.create(
        panier=panier_utilisateur,
        nom_prenoms_client=request.user.get_full_name(),
        total=panier_utilisateur.quantite
    )
    # Rediriger vers la page de génération du reçu/facture
    return redirect('gestionProduit:recu', transaction_id=nouvelle_transaction.id)


def deletePanier(request):
    panier_utilisateur = Panier.objects.get(user=request.user)
    produit_paniers = produitPanier.objects.filter(panierAssocier=panier_utilisateur)
    produit_paniers.delete()
    panier_utilisateur.delete()
    return redirect('gestionProduit:afficher_panier')

def dashboard(request):
    return render(request, 'dashboard.html')

def statistiques_json(request):
    # Statistiques des transactions
    total_ventes = Transaction.objects.aggregate(Sum('total'))['total__sum'] or 0
    total_transactions = Transaction.objects.count()

    # Niveaux de stock
    niveaux_stock = []
    for produit in Produit.objects.all():
        niveaux_stock.append({
            'nom_produit': produit.nom_produit,
            'quantite_produit': produit.quantite_produit,
        })

    # Opérations de vente
    # Vous devez adapter ceci en fonction de la manière dont vous stockez les opérations de vente

    data = {
        'total_ventes': total_ventes,
        'total_transactions': total_transactions,
        'niveaux_stock': niveaux_stock,
    }
    
    return JsonResponse(data)


def validation(request):
    produit_paniers = produitPanier.objects.filter(user=request.user)
    produitAssocier=produitPanier.objects.all()
    nombre_articles_panier = produit_paniers.count()
    return render(request, 'validation.html', {'produit_paniers': produit_paniers, 'produitAssocier':produitAssocier,'nombre_articles_panier': nombre_articles_panier})
