from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Programs

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1', 'password2']

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    program = forms.ModelChoiceField(queryset=Programs.objects.values_list('title', flat=True), to_field_name='title')

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
    

class AddPrograms(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}), max_length=2000)
    timings = forms.CharField(max_length=1000)