from django import forms
from .models import Items



class DonateItemForm(forms.ModelForm):
    class Meta:
        model=Items
        fields=('user','title','location','descreption','image','is_available','is_approved')
        labels={
            'user':'',
            'title':'',
            'location':'',
            'descreption':'',
            'image':'',
            'is_available':'',
            'is_approved':'',
            #'updated_at':'',
        }
        exclude=('user',)

class UpdateItemForm(forms.ModelForm):
    class Meta:
        model=Items
        exclude=('user',)