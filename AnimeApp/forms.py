from django import forms

from .models import Topicinfo

class Topic_form(forms.ModelForm):
    class Meta:
        model = Topicinfo
        fields=["anime","character",
        "quote"
        ]
 