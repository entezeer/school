from django import forms

from .models import Feedback

class FeedBackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        exclude=[]
