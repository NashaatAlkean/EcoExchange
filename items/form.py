from django import forms
from .models import Items



class DonateItemForm(forms.ModelForm):
    class Meta:
        model=Items
        exclude=('user',)

class UpdateItemForm(forms.ModelForm):
    class Meta:
        model=Items
        exclude=('user',)