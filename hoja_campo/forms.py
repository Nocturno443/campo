from django import forms
from .models import Meep
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MeepForm(forms.ModelForm):
   class Meta:
      model=Meep
      
      fields=['domicilio', 'ficha', 'visita','comentarios']
      labels={
         'domicilio':'',
         'ficha':'',
         'visita':'',
         'comentarios': '',

       }
      
      widgets = {
         'domicilio': forms.TextInput(attrs={'placeholder': 'Direccion', 'class':'form-control'}),
         'ficha': forms.TextInput(attrs={'placeholder' : 'Ficha', 'class':'form-select'}),
         'visita': forms.Select(attrs={'placeholder' : 'Visita', 'class':'form-select'}),
         'comentarios': forms.Textarea(attrs={'placeholder' : 'Comentarios', 'class':'form-select'}),

       }


class RevMeepForm(forms.ModelForm):
   class Meta:
      model=Meep
      
      fields=['revisita', 'revisita_fecha', 'ficha_ref','domicilio', 'ficha', 'visita','comentarios']
      labels={
         'revisita':'',
         'fecha revisita':'',
         'ficha revisita':'',
         'domicilio':'',
         'ficha':'',
         'visita':'',
         'comentarios': '',

       }
      
      widgets = {
         'revisita': forms.Select(attrs={'placeholder' : 'reVisita', 'class':'form-select'}),
         'revisita_fecha': forms.DateInput(attrs={'type':'date','class':'form-control'}),  
         'ficha_ref': forms.TextInput(attrs={'placeholder' : 'Ficha Revisita', 'class':'form-select'}),
         'domicilio': forms.TextInput(attrs={'placeholder': 'Direccion', 'class':'form-control'}),
         'ficha': forms.TextInput(attrs={'placeholder' : 'Ficha', 'class':'form-select'}),
         'visita': forms.Select(attrs={'placeholder' : 'Visita', 'class':'form-select'}),
         'comentarios': forms.Textarea(attrs={'placeholder' : 'Comentarios', 'class':'form-select'}),

       }

   
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2')         

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].label = '' 
        self.fields['username'].help_text = '<span class="form-text text-muted"><small> Requerido. 150caracteres maximo</small></spam>'

        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = '' 
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Ingrese una contraseña..</li><li>Que no sea muy larga...</li><li>que no sea muy complicada..</li></ul>'

        self.fields['password2'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repita la Contraseña'
        self.fields['password2'].label = '' 
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small> Repita la contraseña ...</small></spam>'

    



    
       