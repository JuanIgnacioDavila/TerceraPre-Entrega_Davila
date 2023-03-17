from django import forms
from AppEntrega.models import ProductoModel,ClienteModel,TiendaModel





class ProductoForm(forms.ModelForm):
    class Meta:
        model=ProductoModel
        fields="__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model=ClienteModel
        fields="__all__"

class TiendaForm(forms.ModelForm):    
    class Meta:
        model=TiendaModel
        fields="__all__"

class BuscarClienteForm(forms.Form):
    nombre=forms.CharField()
class BuscarProductoForm(forms.Form):
    nombre=forms.CharField()
class BuscarTiendaForm(forms.Form):
    nombre=forms.CharField()
