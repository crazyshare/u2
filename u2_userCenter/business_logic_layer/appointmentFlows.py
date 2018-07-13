#coding=utf-8
#coding=utf-8
import time
from presentation_layer.two_level_page import phoneRepair
class AppointmentFlows():
    '''预约挂号卡片相关操作'''
    def __init__(self,cf):
        self.cf=cf#用户中心首页操作实例
        self.d=self.cf.d
        self.pr=phoneRepair.PhoneRepair(self.d)#手机维修相关页面实例
        pass

    def enter_appointment(self):
        self.cf.ci.title_appointment.click()
        time.sleep(3)
        pass
