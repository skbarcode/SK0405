from stark.service.v1 import  StarkHandler

class CustomerHandler(StarkHandler):
    list_display = ['name', 'address', 'tel', 'meno']