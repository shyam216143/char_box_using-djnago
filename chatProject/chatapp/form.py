from django import forms
from django.forms import ModelForm
from .models import chat_mes


class MessageForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":4, "placeholder": "Type message here"}))
    class Meta:
        model = chat_mes
        fields = ["message",]