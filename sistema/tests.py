from decimal import Decimal

from django.test import TestCase
from .models import Editorial, Libro


class CatalogoTests(TestCase):
	def test_libro_tiene_nombre_y_se_elimina_con_su_editorial(self):
		editorial = Editorial.objects.create(
			nombre='Editorial Sur',
			pais='Chile',
			ciudad='Santiago',
			presupuesto_pesos=Decimal('1500000.00'),
		)
		libro = Libro.objects.create(
			titulo='Historias del Sur',
			autor='Ana Pérez',
			isbn='978-956-000-000-1',
			precio_pesos=Decimal('19990.00'),
			editorial=editorial,
		)

		self.assertEqual(str(editorial), 'Editorial Sur')
		self.assertEqual(str(libro), 'Historias del Sur')

		editorial.delete()

		self.assertFalse(Libro.objects.filter(pk=libro.pk).exists())
