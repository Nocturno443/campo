from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender = User)


ELECCION_FR=[
    (0,'Sin movimiento'),
    (1,'Ausente Total'),
    (2,'Ausente, pero confirma domicilio'),
    (3,'Vivienda desocupada'),
    (4,'Rechazo'),
    (5,'El domicilio No corresponde al beneficiario'),
    (6,'Cambio de domicilio/Se mudaron'),
    (7,'Direccion No hubicable'),
    (9,'Efectiva'),
    (98,'Otra causa'),
]

class Ficha_Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    

class Ficha_Tipo_2(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
   

class Meep(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="meeps", on_delete=models.DO_NOTHING)
    domicilio = models.CharField(max_length=200)
    ficha = models.TextField(max_length=11)
    visita = models.ForeignKey(Ficha_Tipo, on_delete=models.CASCADE,null=True)
    revisita = models.ForeignKey(Ficha_Tipo_2, on_delete=models.CASCADE,null=True)
    revisita_fecha = models.DateField(blank=True, null=True)
    revisita_usuario = models.TextField(max_length=11,default='')
    ficha_ref = models.TextField(max_length=11,default='')
    comentarios = models.TextField(default=0, null=False,blank=False, max_length=200)

    def __str__(self):
        return(
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d}):"
            f"{self.domicilio}:"
            f"{self.ficha}:"
            f"{self.visita}:"
            f"{self.ficha_ref}:"
            f"{self.revisita}"
            f"({self.revisita_fecha:%Y-%m-%d}):"
            f"{self.revisita_usuario}"


        )


