# Generated by Django 4.0 on 2022-03-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumb',
            field=models.ImageField(default='default_product.png', null=True, upload_to=''),
        ),
    ]
