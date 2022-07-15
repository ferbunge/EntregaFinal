from django import forms

class Formulario(forms.Form):

    id = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()