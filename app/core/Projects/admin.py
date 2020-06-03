from django.contrib import admin
from .models import TipoDocu, CategProye, Proyectos, Documentos
# Register your models here.

class TipoDocuModel(admin.ModelAdmin):
    list_display = ["NombDocu"]
    class Meta:
        model = TipoDocu
admin.site.register(TipoDocu)

class CategProyeModel(admin.ModelAdmin):
    list_display = ["Lenguaje"]
    class Meta:
        model = CategProye
admin.site.register(CategProye)

class ProyectoModel(admin.ModelAdmin):
    list_display = ["NombProy"]
    class Meta:
        model = Proyectos
admin.site.register(Proyectos)

class DocumentoModel(admin.ModelAdmin):
    list_display = ["NombDocu"]
    class Meta:
        model = Documentos
admin.site.register(Documentos)