from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.constants import LOGIN_INVALID_MESSAGE

User = get_user_model()


# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]


class UserLoginForm(AuthenticationForm):
    """form for the user login."""

    username = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages.update({
            "invalid_login": LOGIN_INVALID_MESSAGE
        })

    def clean_username(self):
        """validate username."""
        return self.cleaned_data['username'].lower()