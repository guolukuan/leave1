from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
# Create your models here.


class User(AbstractUser, BaseModel):
    '''用户模型类'''

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Message(BaseModel):
    '''请假人信息'''
    user = models.ForeignKey('User', verbose_name='所属账户', on_delete=False)
    name = models.CharField(max_length=20,verbose_name='姓名')
    age = models.CharField(max_length=20,verbose_name='年龄')
    sex = models.CharField(max_length=1,verbose_name='性别')
    serial = models.IntegerField(verbose_name='员工编号')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    section = models.CharField(max_length=20,verbose_name='隶属部门')
    class Meta:
        db_table = 'Message'
        verbose_name = '信息'
        verbose_name_plural = verbose_name