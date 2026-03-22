from django import forms

class LogicForm(forms.Form):
    number = forms.IntegerField(
        label="Enter a Number",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 7'})
    )

class PasswordForm(forms.Form):
    password = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type password...'})
    )

class BusPassForm(forms.Form):
    pass_id = forms.CharField(
        label="Pass ID",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., BUS123'})
    )
