from django.contrib import admin
from .models import *

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Panier)
admin.site.register(produitPanier)
admin.site.register(Transaction)
# Register your models here.
