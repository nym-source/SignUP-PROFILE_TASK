from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_PIC  = models.FileField(blank=True, upload_to='user_images/')
    Category = models.CharField(max_length=200,null=True)
    Full_Address = models.TextField(max_length=500,null=True)
    city   = models.CharField(max_length=200,null=True)
    state   = models.CharField(max_length=200,null=True)
    pincode   = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.city 


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
