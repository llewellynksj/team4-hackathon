from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """A form to add Messages"""
    class Meta:
        model = Message
        fields = ('value',)