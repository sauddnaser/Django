from django import forms
from .models import Rev

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Rev
        fields = ('Email','Name','Product','Title','write')

        widgets = {
            'Email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'E-Mail'}),
            'Name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}),
            'Product': forms.Select(attrs={'class': 'form-control'}),
            'Title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Review Titel'}),
            'write': forms.Textarea(attrs={'class': 'form-control'}),
        }