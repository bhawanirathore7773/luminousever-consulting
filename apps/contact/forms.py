from django import forms
from .models import Lead

class ContactForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields=["name","email","company","phone","message"]
        widgets={"message":forms.Textarea(attrs={"rows":5})}
