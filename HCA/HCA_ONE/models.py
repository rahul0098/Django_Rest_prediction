from django.db import models

# Create your models here.

class imagedb(models.Model):

    file=models.FileField(blank=None, null=False)
