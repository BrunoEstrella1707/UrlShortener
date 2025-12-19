from django import forms
from .models import ShortenedUrl


class ShortUrlForm(forms.ModelForm):

    class Meta:
        model = ShortenedUrl
        fields = ['original_url']
