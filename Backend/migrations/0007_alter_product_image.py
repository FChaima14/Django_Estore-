# Generated by Django 3.2.13 on 2022-07-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]