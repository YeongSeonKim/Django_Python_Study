from django.db import models

# Create your models here.
class Category(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_code = models.CharField(max_length=100, blank=True, null=True)
    c_name = models.CharField(max_length=100, blank=True, null=True)
    i_code = models.CharField(max_length=100, blank=True, null=True)
    i_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'[{self.c_code}] : [{self.i_name}]'


class Product(models.Model):
    p_id = models.IntegerField(primary_key=True)
    c = models.ForeignKey(Category, models.DO_NOTHING)
    p_name = models.CharField(max_length=45, blank=True, null=True)
    img_src = models.URLField(unique=True)
    price = models.IntegerField(null=True, blank=True)
    link = models.URLField(unique=True)

    def __str__(self):
        return f'[{self.c_id}] : [{self.p_name}]'