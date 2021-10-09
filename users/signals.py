from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# @receiver(post_save, sender=Profile)
def profile_created(sender, instance, created, **kwargs):
    print("signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


# @receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("User deleted")


post_save.connect(profile_created, sender=User)
post_delete.connect(profile_deleted, sender=Profile)
