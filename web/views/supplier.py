from stark.service.v1 import  StarkHandler

class SupplierHandler(StarkHandler):
    list_display = ['name', 'address', 'tel', 'meno']