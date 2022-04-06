from stark.service.v1 import site
from web import models

from web.views.userinfo import UserInfoHandler
from web.views.department import DepartmentHandler
from web.views.sort import SortHandler
from web.views.unit import UnitHandler
from web.views.customer import CustomerHandler
from web.views.supplier import SupplierHandler
from web.views.product import ProductHandler
from web.views.company import CompanyHandler

site.register(models.Sort, SortHandler)
site.register(models.Unit, UnitHandler)
site.register(models.Customer, CustomerHandler)
site.register(models.Supplier, SupplierHandler)
site.register(models.Product, ProductHandler)
site.register(models.Company, CompanyHandler)
site.register(models.Department, DepartmentHandler)
site.register(models.UserInfo, UserInfoHandler)