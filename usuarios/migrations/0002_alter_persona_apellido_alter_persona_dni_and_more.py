# Generated by Django 4.2.7 on 2023-11-12 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="persona",
            name="apellido",
            field=models.CharField(max_length=30, verbose_name="apellido"),
        ),
        migrations.AlterField(
            model_name="persona",
            name="dni",
            field=models.PositiveIntegerField(unique=True, verbose_name="dni"),
        ),
        migrations.AlterField(
            model_name="persona",
            name="email",
            field=models.EmailField(max_length=150, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="persona",
            name="nombre",
            field=models.CharField(max_length=30, verbose_name="nombre"),
        ),
    ]
