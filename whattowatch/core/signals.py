from core.models import WatchableContent
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import os

_UNSAVED_FILEFIELD = 'unsaved_filefield'

@receiver(pre_save, sender=WatchableContent)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.poster)
        instance.poster = None

@receiver(post_save, sender=WatchableContent)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        poster =  getattr(instance, _UNSAVED_FILEFIELD)
        instance.poster = poster
        instance.poster.name = os.path.join(str(instance.id), poster.name)
        instance.save()        
        instance.__dict__.pop(_UNSAVED_FILEFIELD)
