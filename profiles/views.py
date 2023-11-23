from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm


def display_profile(request):
  return render(request, 'profile.html', {})


class Registration(SuccessMessageMixin, generic.CreateView):
    """
    Links custom registration form to registration template
    """
    form_class = RegistrationForm
    template_name = 'auth/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Your registration was successful'


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    """
    Displays successfully logged out message when user logs out
    """
    messages.add_message(
        request, messages.INFO, 'You have successfully logged out')
