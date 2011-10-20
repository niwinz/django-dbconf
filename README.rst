=============
django-dbconf
=============

Simple helper to save settings in a database and efficient access to this data through cache.

This application is not intended to replace the django settings. Allows for complex applications 
that claim to have certain settings in the database and to change the flight, and especially to 
have them with persistence.

Its use is very simple, containing a model with 2 fields (key, val) and a singleton class 
(with cache) to serve as interface to the configuration.

The key is in a namespace, so code can be searched by, or at least I call it so. 

Example:
--------

* 'google.analytics.code'
* 'google.analytics.domain'

Example of usage config object:
-------------------------------

    >>> from django_dbconf.conf import config
    >>> val = config.get('google.analytics.code')

Example of obtain all config by prefix:
---------------------------------------

    >>> print list(config.get_range('google.')
    [('google.analytics.code', 'XXXXX'), ('google.analytics.domain', '.niwi.be')]


**config** is a instance of a `LazyDatabaseConf` and the public method are:

* get(key, default=None) -> str:  get key if not exists in cache obtain key and value pair from database.
* set(key, value) -> None: only modifies in memory and cache, not database modification
* get_range(prefix) -> generator: get all key value pairs searching by prefix.

**NOTE**: If value is modified in database, the cache is invalidated and config object always 
returns the updated value.
