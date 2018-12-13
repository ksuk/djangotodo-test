from django import forms
from todo.models import Posting

class PostingForm(forms.ModelForm):

    class Meta:
        model = Posting
        fields = ("message",)
        widgets = {"message":forms.Textarea(attrs={"cols":40, "row":4})}