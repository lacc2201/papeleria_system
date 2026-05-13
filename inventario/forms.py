from django import forms
from .models import Producto, Venta


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'nombre',
            'categoria',
            'precio_venta',
            'cantidad',
            'imagen'
        ]

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),

            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),

            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio de venta'
            }),

            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad disponible'
            }),

            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'capture': 'environment'
            }),

        }


class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta

        fields = [
            'producto',
            'cantidad'
        ]

        widgets = {

            'producto': forms.Select(attrs={
                'class': 'form-select'
            }),

            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad vendida'
            }),

        }