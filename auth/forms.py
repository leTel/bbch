from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'autofocus': 'autofocus',}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'id': 'email_field'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    passwordCheck = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    new_account = forms.BooleanField(initial=False, required=False, label="Create new account")
    remember = forms.BooleanField(initial=True, required=False, label='Remember me')

class ProfileForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(required=False,)
    last_name = forms.CharField(required=False,)
