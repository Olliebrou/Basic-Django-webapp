from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    signature = models.CharField(max_length=120, default= "Be good. ")
    date = models.DateTimeField()

def __str__(self):
    return self.title

