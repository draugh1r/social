from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )

    def __str__(self):
        return str(self.username)
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(username=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()