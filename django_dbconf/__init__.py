# -*- coding: utf-8 -*-

from django.utils.functional import SimpleLazyObject
from .conf import LazyDatabaseConf

config = SimpleLazyObject(lambda: LazyDatabaseConf())

__version__ = (0, 1, 0, 'dev', 0)
