from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Share Your News",
                "class":"form-control",
            }
        ),
        label="",
        )
    class Meta:
        model = News
        exclude = ("user",)
