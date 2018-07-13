#coding=utf-8
from presentation_layer import page
class ApplianceRepair(page.Page):
    '''家电维修相关页面'''
    def __init__(self, d):
        page.Page.__init__(self, d)
        pass


    '''
    家电清洗
    '''
    @property
    def btn_settlement(self):
        return self.d(description=u"去结算")

    '''
    家电维修
    '''
    @property
    def btn_settlement(self):
        return self.d(description=u"确认购买")

    '''
    家电优惠福利
    '''
    @property
    def btn_get_discount(self):
        return self.d(description=u"领取优惠券")

    '''
    家电安装页面
    '''
    @property
    def btn_settlement(self):
        return self.d(description=u"确认购买")

    '''
    更多服务页面
    '''
    @property
    def btn_order(self):
        return self.d(description=u"订单")