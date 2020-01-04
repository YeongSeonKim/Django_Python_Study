from django.db import models


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return f'[{self.pk}번]:{self.title}'
