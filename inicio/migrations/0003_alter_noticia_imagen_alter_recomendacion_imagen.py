# Generated by Django 4.2.4 on 2023-10-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_noticia_imagen_alter_recomendacion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(upload_to='noticias'),
        ),
        migrations.AlterField(
            model_name='recomendacion',
            name='imagen',
            field=models.ImageField(upload_to='recomendaciones'),
        ),
    ]