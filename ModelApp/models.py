from django.db import models
from django.utils import timezone


class BaseMeta(models.Model):
    create_at=models.DateTimeField(default=timezone.datetime.now)
    update_at=models.DateTimeField(default=timezone.datetime.now)
    create_id = models.CharField(max_length=30,default='system')
    update_id = models.CharField(max_length=30,default='system')

    class Meta:
        abstract = True


class Person(BaseMeta):
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True)
    memo = models.TextField()
    web_site = models.URLField(null=True,blank=True)

    class Meta:
        db_table = 'person'
        index_together =[['first_name','last_name']]
        ordering =['salary']




