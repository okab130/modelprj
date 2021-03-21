import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')

from django import setup
setup()

from ModelApp.models import Person

p = Person(
    first_name='Taro',last_name='Sato',
    birthday='2000-01-01',email='a@a.co.jp',
    salary=None,memo='memo taro',web_site='http://www.google.com'
)
p.save()
