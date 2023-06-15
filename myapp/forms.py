from django import forms
from .models import Student
class StudentCF(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'