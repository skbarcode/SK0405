# Generated by Django 3.2.10 on 2022-04-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20220404_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edit_time', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='客户')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='地址')),
                ('tel', models.CharField(blank=True, max_length=13, null=True, verbose_name='电话')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='手机号码')),
                ('meno', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='计量单位')),
            ],
            options={
                'verbose_name': '计量单位',
                'verbose_name_plural': '计量单位',
            },
        ),
    ]