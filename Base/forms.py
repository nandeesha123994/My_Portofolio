from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your number'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 5}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2 or len(name) > 30:
            raise forms.ValidationError("Length of name should be between 2 and 30 characters")
        return name

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if not number.isdigit() or len(number) < 10 or len(number) > 13:
            raise forms.ValidationError("Invalid number, please enter a valid phone number")
        return number
