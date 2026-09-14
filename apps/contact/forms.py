from django import forms
from .models import Lead
class ContactForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields=["name","email","company","phone","message"]
        widgets={"message":forms.Textarea(attrs={"rows":6})}
    def clean_name(self): return self.cleaned_data["name"].strip()
    def clean_message(self): return self.cleaned_data["message"].strip()
