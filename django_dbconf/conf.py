# -*- coding: utf-8 -*-

from django.utils.functional import SimpleLazyObject
from django.conf import settings
from django.core.cache import get_cache

from .models import Conf

class Singleton(type):
    """ Singleton metaclass. """

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)
 
    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args,**kw)
        return cls.__instance


class LazyDatabaseConf(object):
    """
    Class that holds in memory all the settings that are in the database and is updated if something changes,
    the object is totally lazy.
    """

    __metaclass__ = Singleton

    def __init__(self):
        self._cache_name = getattr(settings, 
            'DBCONF_CACHE_ALIAS', 'default')
        self._cache_timeout = getattr(settings,
            'DBCONF_DEFAULT_TIMEOUT', 6000)
        self.cache = get_cache(self._cache_name)

    def set(self, key, value):
        if value and key:
            self.cache.delete(key)
            self.cache.set(key, value, self._cache_timeout)

    def get_range(self, prefix):
        for item in Conf.objects.filter(key__istartswith=prefix).iterator():
            yield (item.key, item.val)

    def get(self, key, default=None):
        value = self.cache.get(key)
        if value:
            return value

        try:
            qsres = Conf.objects.get(pk=key)
            key, value = qsres.key, qsres.value
            self.cache.set(key, value, self._cache_timeout)
            return value
        except Conf.DoesNotExist:
            return default

config = LazyDatabaseConf()
