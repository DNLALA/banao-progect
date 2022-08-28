from email.headerregistry import Address
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    PERSON_TYPE = (
        (1, 'Patient'),
        (2, 'Doctor'),
    )
    Person = forms.ChoiceField(
        choices=PERSON_TYPE,
        widget=forms.RadioSelect()
    )
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    Profile_picture = forms.ImageField()
    email = forms.EmailField()
    Address = forms.CharField()

    class Meta:
        model = User
        fields = ['Person', 'First_Name', 'Last_Name', 'username',
                  'email', 'password1', 'password2']
