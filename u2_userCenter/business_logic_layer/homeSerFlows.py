#coding=utf-8
import time
from presentation_layer.two_level_page import applianceRepair
class HomeSerFlows():
    '''家电服务卡片相关操作'''
    def __init__(self,cf):
        self.cf=cf
        self.d=self.cf.d
        self.ar=applianceRepair.ApplianceRepair(self.d)#家电维修相关页面实例
        pass

    def enter_clear(self):
        self.cf.ci.text_clear_appliance().click()
        time.sleep(3)
        pass

    def enter_fix(self):
        self.cf.ci.text_fix_appliance().click()
        time.sleep(3)
        pass

    def enter_install(self):
        self.cf.ci.text_install_appliance().click()
        time.sleep(3)
        pass

    def enter_discount(self):
        self.d.click(self.cf.ci.point_get_discount()[0], self.cf.ci.point_get_discount()[1])
        time.sleep(3)
        pass

    def enter_more(self):
        self.d.click(self.cf.ci.point_get_more_service()[0],self.cf.ci.point_get_more_service()[1])
        time.sleep(3)
        pass