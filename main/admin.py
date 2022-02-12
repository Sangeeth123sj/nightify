from django.contrib import admin
from django.contrib.auth import get_user_model
from users.models import User
from .models import Picture
# Register your models here.
admin.site.register(User)
admin.site.register(Picture)