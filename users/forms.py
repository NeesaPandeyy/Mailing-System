from django import forms
from django.contrib.auth import get_user_model,authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    role = forms.ChoiceField(choices=[('admin', 'Admin'), ('customer', 'Customer')])  

    class Meta:
        model = User
        fields = ['username','email','role','password1','password2']



class LoginForm(AuthenticationForm):
    role = forms.ChoiceField(choices=[('admin','Admin'),('customer','Customer')])
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        role = cleaned_data.get('role')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.role != role:
                raise ValidationError("Role does not match the user credentials.")
        return cleaned_data