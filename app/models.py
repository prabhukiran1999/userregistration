from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class profiel(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profiel_pic=models.ImageField()