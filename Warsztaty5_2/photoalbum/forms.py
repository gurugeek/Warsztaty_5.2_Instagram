from django import forms
from .models import *


class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['content', 'path']
        labels = {
            "content": "Opisz swój Insta", "path": ""}


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'sent_to']


class SendMessageToUserForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']