from django import forms
from .models import Image

#Create a empty form for the Image database table
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            "imgName",
            "imgFile",
        ]
