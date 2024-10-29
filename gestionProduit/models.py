from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_categorie


class Produit(models.Model):
    nom_produit = models.CharField(max_length=255)
    quantite_produit = models.PositiveIntegerField()
    prix = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='produit_images', blank=True, null=True)
    #image = models.CharField(max_length=255, blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    #est_vendu=models.BooleanField(default=False)
    est_vendu = models.BooleanField(default=False, null=True, blank=True)
    creer_a=models.DateTimeField(auto_now_add=True ,null=True)
    
    def __str__(self):
        return f"{self.nom_produit} - {self.quantite_produit} - {self.prix}"


class Panier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    produits = models.ManyToManyField(Produit, through="produitPanier")
    quantite = models.PositiveIntegerField(default=1) 
 
    def __str__(self):
        return f"{self.user.username}"
    
    
class produitPanier(models.Model):
    panierAssocier=models.ForeignKey("Panier", on_delete=models.CASCADE)
    produitAssocier=models.ForeignKey("Produit", on_delete=models.CASCADE)
    quantite_produit = models.PositiveIntegerField(default=1) 
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    
    def __str__(self):
        return f"{self.produitAssocier}"



class Transaction(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    nom_prenoms_client = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.nom_prenoms_client} - {self.date} - {self.total}"

