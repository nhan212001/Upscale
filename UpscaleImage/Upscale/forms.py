from email.mime import image
from django import forms
from .models import Image

class UploadForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        allow_empty_file=True,
    )
    class Meta:
        model = Image
        fields = [
            'image'
            ]

