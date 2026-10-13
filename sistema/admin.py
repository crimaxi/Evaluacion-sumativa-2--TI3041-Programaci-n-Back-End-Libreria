from django.contrib import admin
# Register your models here.
from .models import Editorial, Libro


def _formatear_pesos(monto):
	return f"${monto:,.0f}".replace(',', '.')


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'pais', 'ciudad', 'presupuesto_en_pesos')
	search_fields = ('nombre', 'pais', 'ciudad')

	@admin.display(description='Presupuesto (CLP)')
	def presupuesto_en_pesos(self, obj):
		return _formatear_pesos(obj.presupuesto_pesos)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'editorial', 'precio_en_pesos')
	list_filter = ('editorial',)
	search_fields = ('titulo', 'autor', 'isbn')

	@admin.display(description='Precio (CLP)')
	def precio_en_pesos(self, obj):
		return _formatear_pesos(obj.precio_pesos)
