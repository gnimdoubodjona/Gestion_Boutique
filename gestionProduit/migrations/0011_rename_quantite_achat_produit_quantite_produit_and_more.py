# Generated by Django 4.2.3 on 2024-01-11 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProduit', '0010_rename_produit_panier_produits_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='quantite_achat',
            new_name='quantite_produit',
        ),
        migrations.RenameField(
            model_name='produitpanier',
            old_name='quantite_achat',
            new_name='quantite_produit',
        ),
    ]
