from account.models import User
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, UserCreationForm, AuthenticationForm

from container.models import MarkupKey
from project.constants import USED_MARKUP_KEY, INVALID_MARKUP_KEY, INACTIVE_MARKUP_KEY


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Markup Key here' }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'gender', 'email', 'password1', 'password2',)

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean_username(self):
        username = self.cleaned_data['username']
        markup_key = MarkupKey.objects.filter(markup_key=username).first()
        if markup_key:
            if markup_key.is_used:
                raise forms.ValidationError(USED_MARKUP_KEY)
            else:
                if not markup_key.is_active:
                    raise forms.ValidationError(INACTIVE_MARKUP_KEY)
                return username
        else:
            raise forms.ValidationError(INVALID_MARKUP_KEY)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': "First Name"})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': "Last Name"})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': "Markup Key"})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "example@xyz.com", "style": "text-transform: lowercase;"})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "Passsword"})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "Confirm Password"})
        self.fields['password1'].help_text = "Use 8 or more characters with mix of letters, numbers & symbols"
        self.fields['email'].help_text = None
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})


class EmailValidationOnForgotPassword(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "example@xyz.com", "style": "text-transform: lowercase;"})

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with this email!")

        return email

    # def send_mail(self, subject_template_name, email_template_name,
    #               context, from_email, to_email, html_email_template_name=None):
    #     print('hjaffdfADHFJFDHFHJH')
    #     context['user_name'] = context.get('user').first_name + ' ' + context.get('user').last_name
    #     del context['user']


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', "style": "text-transform: lowercase;"})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', "style": "text-transform: lowercase;"})
