from django.db import models


# Create your models here.
class PreviousProjects(models.Model):
    name = models.CharField(max_length=40)
    shortDescription = models.TextField(max_length=100)
    largeDescription = models.TextField(max_length=4000)
    appLink = models.TextField(max_length=50)
