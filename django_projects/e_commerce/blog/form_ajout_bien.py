from django import forms
from .models import Offre


class Offresform(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ['prop_id', 'type_proptiete', 'surface', 'nbr_chambre', 'nbr_sallebain', 'type', 'address', 'price', 'existe', 'image']
        

