# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import unique_slug_generator
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from .validators import validate_category
# Create your models here.

User = settings.AUTH_USER_MODEL

class RestaurantLocation(models.Model):
    owner     = models.ForeignKey(User, null=False) #check out Django Models Unleashed JOINCFE.com#class_instance.model_set.all()
    name      = models.CharField(max_length=120)
    location  = models.CharField(max_length=120, null=True, blank=True)
    category  = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    slug      = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def restaurant_location_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def restaurant_location_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#     instance.save()

pre_save.connect(restaurant_location_pre_save_receiver, sender=RestaurantLocation)

# post_save.connect(restaurant_location_post_save_receiver, sender=RestaurantLocation)