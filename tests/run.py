# -*- coding: utf-8 -*-


from django.conf import settings

import sys
import os

test_settings = {
    'DATABASES': {
        'default': {
            'ENGINE':'django.db.backends.sqlite3',
            'USER': '',
            'NAME': '',
            'HOST': '',
            'PORT': '',
        }
    },
    'INSTALLED_APPS': [
        'tests.general_app',
        'django_dbconf',
    ],
    'CACHE': {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            #'LOCATION': 'unique-snowflake',
        }
    },
    'ROOT_URLCONF': 'tests.test_app.urls',
    'LOGGING': {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console':{ 'level':'DEBUG', 'class':'logging.StreamHandler'}
        },
        'loggers': {
            'django': {
                'handlers':['null'],
                'propagate': False,
                'level':'INFO',
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            }
        }
    }
}


if __name__ == '__main__':
    test_args = sys.argv[1:]
    if not test_args:
        test_args = ['general_app']

    current_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )

    sys.path.insert(0, current_path)
    if not settings.configured:
        settings.configure(**test_settings)

    from django.test.simple import DjangoTestSuiteRunner

    runner = DjangoTestSuiteRunner(verbosity=2, interactive=True, failfast=False)
    failures = runner.run_tests(test_args)
    sys.exit(failures)
