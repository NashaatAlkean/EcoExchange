from django import forms
from .models import Items



class DonateItemForm(forms.ModelForm):
    class Meta:
        model=Items
        fields=('user','title','location','descreption','image','is_available')
        labels={
            'user':'',
            'title':'',
            'location':'',
            'descreption':'',
            'image':'',
            'is_available':'',
            #'updated_at':'',



        }
        exclude=('user',)

class UpdateItemForm(forms.ModelForm):
    class Meta:
        model=Items
        exclude=('user',)