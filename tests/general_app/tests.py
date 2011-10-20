# -*- coding: utf-8 -*-

from django.test import TestCase  
from django_dbconf.conf import config
from django_dbconf.models import Conf

from django.db import connection

class DatabaseConfTest(TestCase):
    def setUp(self):
        Conf.objects.all().delete()
        self.conf = [
            Conf.objects.create(key='test.a.a', val='123'),
            Conf.objects.create(key='test.a.b', val='234'),
            Conf.objects.create(key='test2.a.a', val='123')
        ]

    def test_get_key(self):
        with self.assertNumQueries(0):
            val = config.get('test.a.a')
            self.assertEqual(val, '123')
    
    def test_get_key_with_saving(self):
        with self.assertNumQueries(3):
            cfg = Conf.objects.get(key='test.a.a')
            cfg.val = '333'
            cfg.save()

            val = config.get('test.a.a')
            self.assertEqual(val, '333')

            val = config.get('test.a.a')
            self.assertEqual(val, '333')
    
    def test_get_range(self):
        values = list(config.get_range('test.'))
        self.assertEqual(len(values), 2)
