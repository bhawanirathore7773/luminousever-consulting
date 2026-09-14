from django import forms
class AssessmentLeadForm(forms.Form):
    name=forms.CharField(max_length=160)
    email=forms.EmailField()
    company=forms.CharField(max_length=200,required=False)
    def clean_name(self): return self.cleaned_data["name"].strip()
