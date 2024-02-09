from django.db import models
from django.contrib.auth.models import User
import os
import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, blank=True)
    query = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    profile_image = models.ImageField(
        default='media/default.jpg', upload_to='media', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


def filepath(request, filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timenow, old_filename)
    return os.path.join('uploads/', filename)


class Review(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=200, blank=True)
    review = models.TextField(max_length=500, blank=True)
    product_image = models.ImageField(
        upload_to=filepath, null=True, blank=True)

    def __str__(self):
        return f"{self.name}'s review"
