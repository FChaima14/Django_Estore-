# Generated by Django 3.2.13 on 2022-06-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport Wear'), ('Ow', 'Outwear')], default='p', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='S', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('p', 'primary'), ('S', 'secondary'), ('d', 'danger')], default='P', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
