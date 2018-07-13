#coding=utf-8
from presentation_layer import page
class PhoneRepair(page.Page):
    '''手机维修相关页面元素'''

    def __init__(self,d):
        page.Page.__init__(self,d)
        pass

    '''
    订单状态页面
    '''
    @property
    def title_order(self):
        return self.d(resourceId="com.paic.example.simpleapp:id/rym_title_textview", textContains=u'订单状态')

    '''
    全部订单页面
    '''
    @property
    def text_phone(self):
        return self.d(description=u"客服电话：4008-112-112")

    '''
    维修预约页面
    '''
    @property
    def text_repair_appointment(self):
        return self.d(description=u"维修预约")
