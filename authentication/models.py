from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone = models.CharField(max_length=256, blank=True, null=True)
   # gender = models.CharField(max_length=1, choices=(('m',  ('Male')), ('f', ('Female'))),blank=True, null=True)
   
   

		
		
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

