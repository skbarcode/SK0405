from stark.service.v1 import  StarkHandler

class ProductHandler(StarkHandler):
    list_display = ['name', 'unit', 'sort', 'meno']