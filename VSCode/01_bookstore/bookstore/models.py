from django.db import models

# Create your models here.
class Book(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return f'[{self.code}번] : [책이름 : {self.name}]'