from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofcus ':'True',
    'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
    'class':'form-control'}))



class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofcus ':'True',
    'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
       model = User
       fields = ['username','email','password1','password2']

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))

     

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs=
        {'autofocus':'True','autocomplete':'current-password','class':'form-control'}
    ))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs=
        {'autocomplete':'current-password','class':'form-control'}
    ))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs=
        {'autocomplete':'current-password','class':'form-control'}
    ))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['name','locality','city','mobile','zipcode']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
        }
class ResetPasswordForm(PasswordResetForm):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
    
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name) -> None:
        return super().send_mail(subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name)

class ResetPasswordConfirmForm(forms.Form):
    new_password1 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    new_password2 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        

    def clean_new_password1(self, *args, **kwargs):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.data.get('new_password2')
        
        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError("Password mismatch")

        return new_password1

    def save(self, commit=True, *args, **kwargs):
        self.user.set_password(self.cleaned_data.get('new_password1'))

        if commit:
            self.user.save()

        return self.user        