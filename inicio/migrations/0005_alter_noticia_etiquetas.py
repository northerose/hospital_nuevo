# Generated by Django 4.2.7 on 2023-11-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inicio", "0004_etiquetas_noticia_etiquetas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="noticia",
            name="etiquetas",
            field=models.ManyToManyField(blank=True, to="inicio.etiquetas"),
        ),
    ]