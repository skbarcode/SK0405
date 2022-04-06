from django.db import models
from rbac.models import UserInfo as RbacUserInfo


class Main(models.Model):
    last_edit_time = models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        abstract = True


class Sort(Main):
    # sid = models.BigAutoField(primary_key=True, verbose_name='编号', )
    title = models.CharField(max_length=32, unique=True, verbose_name='分类')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Unit(models.Model):
    # sid = models.BigAutoField(primary_key=True, verbose_name='编号', )
    title = models.CharField(max_length=32, unique=True, verbose_name='计量单位')

    class Meta:
        verbose_name = '计量单位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Customer(Main):
    name = models.CharField(max_length=64, unique=True, verbose_name='客户')
    address = models.CharField(max_length=128, verbose_name='地址', blank=True, null=True)
    tel = models.CharField(max_length=13, verbose_name="电话", blank=True, null=True)
    phone = models.CharField(max_length=13, verbose_name="手机号码", blank=True, null=True)
    meno = models.CharField(max_length=128, verbose_name='备注', default='', blank=True, null=True)

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Supplier(Main):
    name = models.CharField(max_length=64, unique=True, verbose_name='供应商')
    address = models.CharField(max_length=128, verbose_name='地址', blank=True, null=True)
    tel = models.CharField(max_length=13, verbose_name="电话", blank=True, null=True)
    phone = models.CharField(max_length=13, verbose_name="手机号码", blank=True, null=True)
    meno = models.CharField(max_length=128, verbose_name='备注', default='', blank=True, null=True)

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(Main):
    name = models.CharField(max_length=64, verbose_name='品名规格', )
    unit = models.ForeignKey(Unit, verbose_name='单位', on_delete=models.DO_NOTHING, blank=True, null=True)
    sort = models.ForeignKey(Sort, verbose_name='分类', on_delete=models.DO_NOTHING)
    meno = models.CharField(max_length=128, verbose_name='备注', default='', blank=True, null=True)

    class Meta:
        verbose_name = '品名规格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=64, verbose_name='公司名称')
    entitle = models.CharField(max_length=64, verbose_name='companytitle')
    address = models.CharField(max_length=128, verbose_name='地址')
    tel = models.CharField(max_length=16, verbose_name='公司电话')
    fax = models.CharField(max_length=16, verbose_name='公司传真')
    slug = models.URLField(verbose_name='公司网址')
    email = models.EmailField(verbose_name='公司邮箱')
    bank_name = models.CharField(max_length=32, verbose_name='银行名称')
    account_title = models.CharField(max_length=32, verbose_name='帐户名称')
    bank_account = models.CharField(max_length=32, verbose_name='银行帐户')
    bank_number = models.CharField(max_length=24, verbose_name='银行行号')
    logo = models.ImageField(upload_to='images/', verbose_name="LOGO", )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '公司信息'
        verbose_name_plural = verbose_name


class Department(Main):
    title = models.CharField(max_length=12, verbose_name='部门')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name


class UserInfo(RbacUserInfo):
    nickname = models.CharField(verbose_name='姓名', max_length=16)
    phone = models.CharField(verbose_name='手机', max_length=16)
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(verbose_name='性别', choices=gender_choices, default=1)
    depart = models.ForeignKey(to="Department",on_delete=models.CASCADE,verbose_name='部门')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name