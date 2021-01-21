from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    # this function is used for styling the form on front-end
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update(
    #         {'class': 'zmdi zmdi-account material-icons-name'})
    #     self.fields['email'].widget.attrs.update({'class': 'zmdi zmdi-email'})
    #     self.fields['password1'].widget.attrs.update(
    #         {'class': 'zmdi zmdi-lock'})
    #     self.fields['password2'].widget.attrs.update(
    #         {'class': 'zmdi zmdi-lock-outline'})

    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
