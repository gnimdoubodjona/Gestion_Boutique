# Generated by Django 5.0.1 on 2024-01-14 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProduit', '0016_panier_quantite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='panier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionProduit.panier'),
        ),
    ]
