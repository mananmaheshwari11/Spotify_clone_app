from django import forms
from .models import Library
from django.contrib.auth.models import User
class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }