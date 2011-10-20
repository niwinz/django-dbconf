from setuptools import setup, find_packages

description="""
Simple helper to save settings in a database and efficient access to this data through cache.
"""

long_description = ""


setup(
    name="django-dbconf",
    version=':versiontools:django_dbconf:',
    url='https://github.com/niwibe/django-dbconf',
    license='BSD',
    platforms=['OS Independent'],
    description = description.strip(),
    long_description = long_description.strip(),
    author = 'Andrei Antoukh',
    author_email = 'niwi@niwi.be',
    maintainer = 'Andrei Antoukh',
    maintainer_email = 'niwi@niwi.be',
    packages = [
        'django_dbconf',
    ],
    include_package_data = True,
    install_requires=[
        'distribute',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    zip_safe = False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
