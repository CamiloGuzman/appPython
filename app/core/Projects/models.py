from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import DatosUser
# Create your models here.

class TipoDocu(models.Model):
    NombDocu = models.CharField(max_length = 45, null=True, verbose_name="Tipo Documento")
    
    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipos de Documento"
    
    def __str__(self):
        return self.NombDocu
    
class CategProye(models.Model):
    Lenguaje = models.CharField(max_length = 45, null=True, verbose_name = "Lenguaje de Programacion")
    MotorDB = models.CharField(max_length = 45, null=True, verbose_name = "Base de Datos")
    Arquitectura = models.CharField(max_length = 45, null=True, verbose_name = "Arquitectura de Software")
    
    class Meta:
        verbose_name = "Categoria Proyecto"
        verbose_name_plural = "Categorias de Proyectos"
    
    def __str__(self):
        self.Lenguaje
    
    
class Proyectos(models.Model):
    idCategProye = models.ForeignKey(CategProye, on_delete = models.CASCADE)
    NombProy = models.CharField(max_length = 45, null=True)
    DescProy = models.TextField(verbose_name="Descripcion del proyecto")
    ImgProye = models.ImageField(default= 'img.png', upload_to=None, verbose_name="Imagen del proyecto")
    FechaIni = models.DateField(auto_now_add = True, null=True, verbose_name= "Creado el")
    FechaFin = models.DateField(auto_now_add = True, null=True, verbose_name= "Finalizado el")
    UrlRepo = models.TextField(verbose_name="Ruta del Repositorio")
    EstaProy = models.CharField(max_length = 45, null=True, verbose_name = "Estado del proyecto")
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    
    def __str__(self):
        return self.NombProy
    

class Documentos(models.Model):
    idDocu= models.ForeignKey(TipoDocu, on_delete = models.CASCADE)
    idProyectos = models.ForeignKey(Proyectos, on_delete = models.CASCADE)
    idUsuario = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    NombDocu = models.CharField(max_length = 45, null=True, verbose_name = "Nombre del Documento")
    PathDocu = models.FileField(upload_to = None, verbose_name = "Documento")
    
    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
    
    def __str__(self):
        return self.NombDocu
