# Generated by Django 3.2.13 on 2022-07-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0005_product_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('S', 'Shoeses'), ('SW', 'Sport'), ('Ow', 'Outwear'), ('W', 'Watches'), ('C', 'Causal'), ('H', 'Huts')], max_length=2, null=True),
        ),
    ]
