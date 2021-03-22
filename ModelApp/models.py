from django.db import models
from django.utils import timezone


class BaseMeta(models.Model):
    create_at=models.DateTimeField(default=timezone.datetime.now,verbose_name="作成日時")
    update_at=models.DateTimeField(default=timezone.datetime.now,verbose_name="更新日時")
    create_id = models.CharField(max_length=30,default='system',verbose_name="作成者")
    update_id = models.CharField(max_length=30,default='system',verbose_name="更新者")

    class Meta:
        abstract = True


class Person(BaseMeta):
    first_name = models.CharField(max_length=30,verbose_name="社員姓")
    last_name= models.CharField(max_length=30,verbose_name="社員名")
    birthday = models.DateField(default='1900-01-01',verbose_name="誕生日")
    email = models.EmailField(db_index=True,verbose_name="メール")
    salary = models.FloatField(null=True,verbose_name="年商")
    memo = models.TextField(verbose_name="メモ")
    web_site = models.URLField(null=True,blank=True,verbose_name="WWWサイト")

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'person'
        index_together =[['first_name','last_name']]
        ordering =['salary']

class Customer(BaseMeta):
    customer_name = models.CharField(max_length=30,verbose_name="顧客名")
    customer_email = models.EmailField(db_index=True,verbose_name="メール")
    customer_memo = models.TextField(verbose_name="メモ")
    customer_web_site = models.URLField(null=True,blank=True,verbose_name="wwwサイト")

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'customer'
        ordering =['customer_name']

class Anken(BaseMeta):
    anken_title = models.CharField(max_length=100,verbose_name="案件名")
    anken_customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name="顧客名")
    anken_kianat=models.DateTimeField(default=timezone.datetime.now,verbose_name="起案日")
    syubetu = ((1, '製品販売'),(2, 'SI'), (3, 'コンサル'), (4, 'その他'))
    anken_syubetu = models.IntegerField(choices=syubetu,verbose_name="種別")
    anken_naiyou = models.TextField(verbose_name="内容")

    def __str__(self):
        return self.anken_title

    class Meta:
        db_table = 'anken'
        ordering =['anken_kianat']


class Houmon(BaseMeta):
    houmon_customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name="顧客")
    houmon_anken = models.ForeignKey(Anken, on_delete=models.CASCADE,verbose_name="案件")
    houmon_at=models.DateTimeField(default=timezone.datetime.now,verbose_name="訪問日時")
    mokuteki = ((1, '製品説明'),(2, '案件'), (3, 'クレーム'), (4, '障害'), (5, 'その他'))
    houmon_mokuteki = models.IntegerField(choices=mokuteki,verbose_name="目的種別")
    houmon_memo = models.TextField(verbose_name="メモ")
    houmon_titile = models.CharField(max_length=100,default="訪問目的は必須",verbose_name="訪問タイトル")

    def __str__(self):
        return self.houmon_titile

    class Meta:
        db_table = 'houmon'
        ordering =['houmon_titile']



