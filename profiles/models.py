from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField


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
    category = models.CharField(
        max_length=254, choices=TAG_CATEGORIES, default="Physical")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Profile(models.Model):
    """
    Profile model links to Health Profile
    """
    created_on = models.DateTimeField(auto_now_add=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    pseudonym = models.CharField(
        max_length=100, help_text='Enter the name you would like to be known as to ALL users', default='pseudonym')
    profile_pic = CloudinaryField('image', default='placeholder_k3nekm')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    # health_profile = models.ForeignKey(HealthProfile, on_delete=models.CASCADE)
    # friends = models.ManyToManyField(User, related_name='friends', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.username}"

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        """Function to automatically create a profile when a user is created"""
        if created:
            Profile.objects.create(username=instance)
