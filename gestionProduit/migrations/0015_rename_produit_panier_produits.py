# Generated by Django 5.0.1 on 2024-01-13 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProduit', '0014_rename_produits_panier_produit_alter_produit_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panier',
            old_name='produit',
            new_name='produits',
        ),
    ]
