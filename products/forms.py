from django import forms
from . import models

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'category', 'description', 'serie_number', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Titulo',
            'category': 'Categoria',
            'description': 'Descrição',
            'serie_number': 'Número de Série',
            'location': 'Local',
        }