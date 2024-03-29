# Generated by Django 2.1.8 on 2019-12-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ratify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='请假人')),
                ('department', models.CharField(max_length=100, verbose_name='请假部门')),
                ('phone', models.CharField(max_length=11, verbose_name='请假人手机号')),
                ('sex', models.CharField(max_length=1, verbose_name='请假人性别')),
                ('start_data', models.DateField(verbose_name='起始时间')),
                ('due_date', models.DateField(verbose_name='到期时间')),
                ('cause', models.CharField(max_length=255, verbose_name='请假原因')),
                ('affirm', models.CharField(default='待批准', max_length=10, verbose_name='批准')),
            ],
            options={
                'verbose_name': '请假批准',
                'verbose_name_plural': '请假批准',
                'db_table': 'Ratify',
            },
        ),
    ]
