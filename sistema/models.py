from django.db import models


class Editorial(models.Model):
	nombre = models.CharField(max_length=150)
	pais = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=100)
	presupuesto_pesos = models.DecimalField(max_digits=12, decimal_places=2)

	def __str__(self):
		return self.nombre


class Libro(models.Model):
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=150)
	isbn = models.CharField(max_length=20, unique=True)
	precio_pesos = models.DecimalField(max_digits=10, decimal_places=2)
	editorial = models.ForeignKey(
		Editorial,
		on_delete=models.CASCADE,
		related_name='libros',
	)

	def __str__(self):
		return self.titulo
