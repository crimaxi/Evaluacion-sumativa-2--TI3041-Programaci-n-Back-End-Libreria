from django.contrib import admin
# Register your models here.
from .models import Editorial, Libro

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'pais', 'ciudad', 'presupuesto_pesos')
	search_fields = ('nombre', 'pais', 'ciudad')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'editorial', 'precio_pesos')
	list_filter = ('editorial',)
	search_fields = ('titulo', 'autor', 'isbn')
