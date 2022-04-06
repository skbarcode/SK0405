# Generated by Django 3.2.10 on 2022-04-04 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_customer_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edit_time', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='供应商')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='地址')),
                ('tel', models.CharField(blank=True, max_length=13, null=True, verbose_name='电话')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='手机号码')),
                ('meno', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edit_time', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=64, verbose_name='品名规格')),
                ('meno', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='备注')),
                ('sort', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web.sort', verbose_name='分类')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='web.unit', verbose_name='单位')),
            ],
            options={
                'verbose_name': '品名规格',
                'verbose_name_plural': '品名规格',
            },
        ),
    ]
