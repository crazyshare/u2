#coding=utf-8
import uiautomator2 as u2
import time
from public import util

# 整数相除，返回保留两位小数点的浮点数
n_division=lambda x,y:round(x/float(y),2)

class BaseFlows(object):
    '''操作流基类'''
    def __init__(self):
        self.name=util.get_device_name_from_usb()
        self.d=u2.connect_usb(self.name)
        if not self.d:
            self.d = u2.connect()  # 连接设备
        pass

    def clear_all_app(self):
        '''清除当前及所有后台程序'''
        print 'self.name:%s' % self.name
        self.d.press('recent')
        print 'self.name:%s' % self.name
        if self.name == '8b4235be':
            self.clear_mi5()  # 米5
        elif self.name.startswith('127.0.0.1'):  # 虚拟机
            self.clear_v_yeshen()  # 夜神
        pass

    def clear_mi5(self):
        '''清除后台程序--米5'''
        time.sleep(1)
        while self.d(className='android.view.View').exists:
            time.sleep(1)
            self.d.swipe(0.502, 0.517, 0.502, 0.02)
            time.sleep(1)
            if self.d(resourceId="com.miui.home:id/icon_title", text=u"电话").exists:
                break

    def clear_v_yeshen(self):
        '''清除后台程序--夜色模拟器'''
        if self.d(resourceId="com.android.systemui:id/recent_item", className="android.widget.RelativeLayout").exists:
            for e in self.d(resourceId="com.android.systemui:id/recent_item", className="android.widget.RelativeLayout"):
                w, h = util.get_size(self.d);
                x, y = e.center()
                self.d.swipe(n_division(x, w), n_division(y, h), 0.01, n_division(y, h))
        pass

    def unlock(self):
        '''手机解锁'''
        if not self.d.info.get('screenOn'):
            self.d.screen_on()
            time.sleep(1)
            if self.name== '8b4235be':
                self.unlock_mi5()
            elif self.name == '5LM0216531002430':
                self.d.swipe(0.488, 0.702, 0.488, 0.3)
            else:
                self.d.swipe(0.5, 0.9, 0.5, 0.1)
        pass

    def unlock_mi5(self):
        '''米5解锁'''
        self.d.swipe(0.5, 0.9, 0.5, 0.5)
        self.d(text=u"1").click()
        self.d(text=u"2").click()
        self.d(text=u"3").click()
        self.d(text=u"4").click()
        pass
