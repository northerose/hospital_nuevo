# Generated by Django 4.2.4 on 2023-10-19 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(upload_to='uploads/noticias'),
        ),
        migrations.AlterField(
            model_name='recomendacion',
            name='imagen',
            field=models.ImageField(upload_to='uploads/recomendaciones'),
        ),
    ]
