from django.db import models


TAG_CATEGORIES = [
    "Physical",
    "Emotional",
    "Psychological",
]

class tag(models.Model):
    """Model definition for tag."""

    class Meta:
        verbose_name_plural = "Tags"  # Admin panel name

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    category = models.CharField(max_length=254, choices=TAG_CATEGORIES, default="Physical")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name