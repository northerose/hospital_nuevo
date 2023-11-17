from django.db import models

# Create your models here.


class Etiquetas(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias')
    fecha = models.DateField()
    fuente = models.CharField(max_length=200)
    etiquetas = models.ManyToManyField(Etiquetas, blank=True)

    def __str__(self):
        return self.titulo



class Recomendacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='recomendaciones')
    fecha = models.DateField(auto_now=True)
    fuente = models.CharField(max_length=200)

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

