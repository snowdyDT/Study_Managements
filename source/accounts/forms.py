from django import forms 
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label=('Password'), 
        required=True, 
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Write password'})
    )

    password_confirm = forms.CharField(
        label=("Confirm password"), 
        required=True, 
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password_confirm != password_confirm:
            raise forms.ValidationError("Passwords are not equal")
        return cleaned_data 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta: 
        model = User 
        fields = [
            'username', 
            'first_name', 'last_name', 
            'email', 
            'password', 'password_confirm'
        ]