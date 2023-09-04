"""THis file contains model forms of a user and room model."""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from chat.models import Room


class SignupForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and password.
    """

    def __init__(self, *args, **kwargs):
        """
        This method will initialize custom class.
        """
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options, verbose_name, and a lot of other options.
        """
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """
    This is a login form to authenticate user.
    """

    def __init__(self, *args, **kwargs):
        """
        This method will initialize custom class.
        """
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class RoomForm(forms.ModelForm):
    """
    This is a model form for a room model.
    """

    def __init__(self, *args, **kwargs):
        """
        This method will initialize custom class.
        """
        super(RoomForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options, verbose_name, and a lot of other options.
        """
        model = Room
        fields = ['name', 'users']
