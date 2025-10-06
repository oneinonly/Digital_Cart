from django.db import models

# Create your models here.
 class category(models.Model):
    category_name = models.CharField(max_length=50)
    clug = models.CharField(max_length=100, unique=True)