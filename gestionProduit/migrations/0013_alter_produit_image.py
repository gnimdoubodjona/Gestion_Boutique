# Generated by Django 5.0.1 on 2024-01-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProduit', '0012_alter_produit_est_vendu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
