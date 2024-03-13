from django import forms
from website.models import ReviewRating


class ReviewForm(forms.ModelForm):
    class Meta:
        model =ReviewRating
        fields = ['subject','review','rating']
        