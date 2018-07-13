#coding=utf-8
import time,appFlows
from presentation_layer.first_level_page import center_index
from presentation_layer.two_level_page import login_page,jyh_page,nearby_page
from public import util
class CenterFlows(appFlows.AppFlows):
    '''用户中心首页相关业务逻辑操作'''
    def __init__(self,env,host,package):
        appFlows.AppFlows.__init__(self,env,host,package)
        # 添加无需登录的页面实例
        self.ci=center_index.CenterIndex(self.d)#用户中心首页实例
        self.lp=login_page.LoginPage(self.d)#登录页面实例
        self.jyh=jyh_page.JyhPage(self.d)#聚划算页面实例
        self.nb=nearby_page.NearByPage(self.d)#附近页面实例
        pass

    def enter_cener_index(self):
        '''从stg选择页面，进入用户中心插件首页'''
        self.ci.btn_stg2().click_exists(timeout=7.0)#点击用户中心stg2环境
        time.sleep(5)
        return self.d

    def page_to_index(self):
        '''二级页面回到首页'''
        self.d.click(self.ci.option_black()[0],self.ci.option_black()[1])
        time.sleep(2)
        pass

    def page_to_top(self):
        '''首页回到顶部位置'''
        while True:
            if self.d(description=u"全部").exists:
                break
            else:
                self.d.swipe(0.5, 0.1, 0.5, 0.9)
                if self.d(description=u"全部").exists:
                    break
        pass

    def blace_to_top(self):
        self.page_to_index()
        self.page_to_top()
        pass

    def get_by_text(self, text):
        '''在首页，根据文本查找对应位置，若无，则下滑直到页面底部'''
        self.page_to_top()
        time.sleep(1)
        while True:
            e=util.find_e_by_text(self.d,text)
            if e:
                b = e.info.get('visibleBounds')['bottom']
                l = e.info.get('visibleBounds')['left']
                if int(b)>1047:
                    # 若元素bottom<1407,滑动到bottom=936
                    self.d.swipe(l / 1080.00, b / 1920.00, l / 1080.00, 0.5)
                    break
                else:
                    break
            elif self.d(descriptionContains=u'没有发现心仪的内容').exists:
                return False
            else:
                self.d.swipe(0.5, 0.9, 0.5, 0.1)
                pass
        return e

    def login(self, name='18320903651', pwd='qweqwe123'):
        '''登录:18320903651/qweqwe123'''
        self.ci.text_please_login().click_exists(timeout=7.0)
        time.sleep(3)
        self.lp.text_name().send_keys(name)
        time.sleep(1)
        self.lp.text_pwd().send_keys(pwd)
        time.sleep(1)
        self.lp.btn_sub().click()
        time.sleep(5)
        if self.lp.btn_sub:
            self.lp.btn_sub.click()
            time.sleep(5)

    def enter_jyh(self):
        self.ci.text_jyh().click()
        pass

    def enter_nearby(self):
        self.ci.text_nearby().click()

    def click_clear_appliances_no_login(self):
        pass

    def click_clear_appliances_login(self):
        pass

    def click_fix_appliances_no_login(self):
        pass

    def click_fix_appliances_login(self):
        pass

    def click_install_appliances_no_login(self):
        pass

    def click_install_appliances_login(self):
        pass