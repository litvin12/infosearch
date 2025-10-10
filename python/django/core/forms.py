from django import forms
from .models import University

class UniversityForm(forms.ModelForm):
    established_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = University
        fields = ['full_name', 'short_name', 'established_date']
