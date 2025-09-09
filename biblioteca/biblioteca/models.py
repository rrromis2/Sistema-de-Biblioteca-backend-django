from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model): 
    titulo = models.CharField(max_length=150)
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,related_name="libros")
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
