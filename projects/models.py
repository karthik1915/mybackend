from django.db import models


# Create your models here.
class MiniProjectsModal(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.JSONField()  # Use JSONField for storing lists/arrays
    link = models.URLField()
    image_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title
