'''
Django provides a set of built-in signals that let user code get notified by Django itself 
of certain actions. These include some useful notifications

See also:
---------
https://docs.djangoproject.com/en/4.0/topics/signals/


Example from :
______________
https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/
'''

from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import roles

@receiver(post_save, sender=User)
def create_role(sender, instance, created, **kwargs):
    if created:
        roles.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_role(sender, instance, **kwargs):
        instance.roles.save()