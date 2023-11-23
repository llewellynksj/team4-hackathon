from django.db import models
from django_postgres_extensions.models.fields import ArrayField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from . import tags


class Profile(models.Model):
  """
  Profile model links to Health Profile
  """
  created_on = models.DateTimeField(auto_now_add=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  pseudonym = models.CharField(max_length=100, help_text='Enter the name you would like to be known as to ALL users')
  profile_pic = CloudinaryField('image', default='placeholder_k3nekm')
  first_name = models.CharField(max_length=100, null=True, blank=True)
  last_name = models.CharField(max_length=100, null=True, blank=True)
  health_profile = models.ForeignKey(HealthProfile, on_delete=models.CASCADE)
  friends = models.ManyToManyField(User, related_name='friends', blank=True, null=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f"{self.user}"
  
  def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a profile automatically when a User is created
    """
    if created:
        Profile.objects.create(username=instance)


class HealthProfile(models.Model):
  """
  Health Profile of User
  """
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  tags = ArrayField(models.CharField(max_length=255))
  

TAG_CATEGORIES = [
  ("Physical", "Physical"),
  ("Emotional", "Emotional"),
  ("Psychological", "Psychological"),
]

class Tag(models.Model):
  """
  Model definition for tag
  """
  class Meta:
    verbose_name_plural = "Tags"  # Admin panel name

  name = models.CharField(max_length=254)
  friendly_name = models.CharField(max_length=254, null=True, blank=True)
  category = models.CharField(max_length=254, choices=TAG_CATEGORIES, default="Physical")

  def __str__(self):
      return self.name

  def get_friendly_name(self):
      return self.friendly_name
