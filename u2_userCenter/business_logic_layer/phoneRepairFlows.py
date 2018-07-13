#coding=utf-8
import time
from presentation_layer.two_level_page import phoneRepair
class PhoneRepairFlows():
    '''手机维修卡片相关操作'''
    def __init__(self,cf):
        self.cf=cf#用户中心首页操作实例
        self.d=self.cf.d
        self.pr=phoneRepair.PhoneRepair(self.d)#手机维修相关页面实例
        pass

    def enter_order(self):
        self.cf.ci.text_order_info.click()
        time.sleep(3)
        pass

    def enter_all_order(self):
        self.cf.ci.btn_all_order.click()
        time.sleep(3)
        pass

    def enter_repair_appointment(self):
        self.cf.ci.btn_repair_appointment.click()
        time.sleep(3)
        pass
