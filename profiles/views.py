from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm, UpdateProfileForm


class UpdateProfile(SuccessMessageMixin, generic.UpdateView):
    """
    View for updating the profile model
    """
    model = Profile
    template_name = 'update_profile.html'
    form_class = UpdateProfileForm
    success_message = 'Your profile was updated successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # Direct user to their Profile page when form submitted
    # def get_success_url(self) -> str:
    #     return reverse_lazy('profile', kwargs={'pk': self.object.pk})



class ProfileList(generic.ListView):
    """
    Displays all profiles
    """
    model = Profile
    template_name = 'profile_list.html'


class DisplayProfile(generic.DetailView):
  model = Profile
  template_name = 'profile.html'

  def get_context_data(self, *args, **kwargs):
    context = super(
        DisplayProfile, self).get_context_data(
          *args, **kwargs)
    user_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
    context['user_profile'] = user_profile
    return context


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
