from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
  """

  """
  created_on = models.DateTimeField(auto_now_add=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_pic = CloudinaryField('image', default='profile_placeholder')
  first_name = models.CharField(max_length=100, null=True, blank=True)
  last_name = models.CharField(max_length=100, null=True, blank=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f"{self.user}"
  
  def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a profile automatically when a User is created
    """
    if created:
        ParentProfile.objects.create(username=instance)
