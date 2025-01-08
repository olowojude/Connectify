from django.forms import ModelForm
from .models import Link, User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# FOR UPDATE USER FORM
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["profile_image", "bio", "username", "email", ]

# ADD LINK FORM
class AddLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ["name", "url"]