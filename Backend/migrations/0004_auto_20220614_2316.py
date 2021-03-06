# Generated by Django 3.2.13 on 2022-06-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_auto_20220614_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('S', 'Shirt'), ('SW', 'Sport Wear'), ('Ow', 'Outwear')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('p', 'primary'), ('S', 'secondary'), ('d', 'danger')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
