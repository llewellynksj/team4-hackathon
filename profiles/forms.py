from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
  """
  Update profile form
  """
  class Meta:
    model = Profile
    fields = [
      'profile_pic',
      'pseudonym',
    ]
    widgets = {
      'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
      'pseudonym': forms.TextInput(attrs={'class': 'form-control'}),
    }


class RegistrationForm(SignupForm):
  """
  Custom registration form
  """
  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={'class': 'form-control'}))
  first_name = forms.CharField(
    max_length=100, widget=forms.TextInput(
      attrs={'class': 'form-control'}))
  last_name = forms.CharField(
    max_length=100, widget=forms.TextInput(
      attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = (
      'username',
      'first_name',
      'last_name',
      'email',
      'password1',
      'password2')
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def custom_signup(self, request, user):
    user.save()
