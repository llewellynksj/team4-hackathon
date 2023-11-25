from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages
from .models import Profile, Tag
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
    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class ProfileList(generic.ListView):
    """
    Displays all profiles
    """
    model = Profile
    template_name = 'profile_list.html'


def display_profile(request, pk):

    health_concerns_list = Profile.health_concerns.through.objects.filter(
        profile_id=pk)
    tag_list = []
    tag_list_name = []
    for item in health_concerns_list:
        tag_list.append(item.tag_id)
    for item in tag_list:
        tag = Tag.objects.filter(pk=str(item))
        for t in tag:
            tag_list_name.append(t.friendly_name)
            
    print(tag_list_name)
    user_profile = get_object_or_404(Profile, id=pk)

    return render(request, 'profile.html', {
        "health_concerns_list": tag_list_name,
        "profile": user_profile
    }
    )


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
