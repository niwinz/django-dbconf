# -*- coding: utf-8 -*-

from django.dispatch import receiver
from django.db import models
import datetime


class Conf(models.Model):
    key = models.CharField(max_length=255, db_index=True, primary_key=True)
    val = models.TextField(blank=True, null=True, default=None)

    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.last_modified_date = datetime.datetime.now()
        super(Conf, self).save(*args, **kwargs)


@receiver(models.signals.post_save, sender=Conf)
def conf_post_save(sender, instance, **kwargs):
    from .conf import LazyDatabaseConf
    config = LazyDatabaseConf()
    config.set(instance.key, instance.val)
