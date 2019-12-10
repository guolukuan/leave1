from django.db import models
from db.base_model import BaseModel



class Ratify(BaseModel):
    name = models.CharField(max_length=20,verbose_name='请假人')
    department = models.CharField(max_length=100,verbose_name='请假部门')
    phone = models.CharField(max_length=11,verbose_name='请假人手机号')
    sex = models.CharField(max_length=1,verbose_name='请假人性别')
    start_data = models.DateField(verbose_name='起始时间')
    due_date = models.DateField(verbose_name='到期时间')
    cause = models.CharField(max_length=255,verbose_name='请假原因')
    affirm = models.CharField(max_length=10,default='待批准',verbose_name='批准')
    class Meta:
        db_table = 'Ratify'
        verbose_name = '请假批准'
        verbose_name_plural = verbose_name