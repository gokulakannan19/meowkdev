from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
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

        subject = "welcome to Dev search"
        message = "We are glad you are here!"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# @receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
        # print("User deleted")
    except:
        pass


post_save.connect(profile_created, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(profile_deleted, sender=Profile)
