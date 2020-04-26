from django.db import models

# 发布会Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=100)
    limit=models.IntegerField()
    status=models.BooleanField()
    address=models.CharField(max_length=200)
    start_time=models.DateTimeField('events time')
    create_time=models.DateTimeField(auto_now=True)
#当前时间
    def _str_(self):
        return self.name
#嘉宾
class Guest(models.Model):
    event=models.ForeignKey('Event',on_delete=models.CASCADE)
    realname=models.CharField(max_length=64)
    phone=models.CharField(max_length=16)
    email=models.EmailField()
    sign=models.BooleanField()
    create_time=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=("event","phone")

    def _str_(self):
         return self.realname
