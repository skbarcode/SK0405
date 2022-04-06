from stark.service.v1 import  StarkHandler


class CompanyHandler(StarkHandler):
    list_display = ['title', 'entitle', 'address', 'bank_number']