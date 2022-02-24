
from email.policy import default
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Picture(Model):
    upload = models.ImageField(upload_to = 'uploads/')
    converted_picture = models.ImageField(upload_to = 'uploads/', blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    
class Creator(Model):
    portfolio_url = models.URLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)