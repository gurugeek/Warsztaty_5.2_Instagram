from photoalbum.models import Photo
from django import forms


class PhotoAddForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['content', 'path']
        labels = {
            "content": "Opisz swój Insta", "path": ""}