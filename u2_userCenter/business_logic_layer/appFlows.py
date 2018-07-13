#coding=utf-8
import time,baseFlows
from presentation_layer import simpleapp
class AppFlows(baseFlows.BaseFlows):
    '''APP操作'''
    def __init__(self,env,host,package):
        baseFlows.BaseFlows.__init__(self)
        self.package=package
        self.env = env
        self.host = host
        self.app=simpleapp.SimpleApp(self.d)
        pass

    def deal_leaks(self):
        '''
        simple app contains leaks,sometimes leaks will exist
        '''
        time.sleep(1)
        while self.app.title_leaks().exists:
            time.sleep(1)
            if self.app.btn_del_all().exists:
                self.app.btn_del_all().click()
                time.sleep(1)
                self.d(resourceId="android:id/button1").click()
                pass
            else:
                self.clear_all_app()
            self.d.app_start(self.package)
            time.sleep(1)

    def choice_env_host(self):
        '''选择环境、宿主'''
        #若环境是选择的stg2  pass
        if self.app.text_stg2().wait(timeout=2.0):
            pass
        #否则，点击环境选项文本框，选择stg2
        else:
            self.app.text_env.click()
            self.app.text_stg2().click()
            time.sleep(1)
        if self.app.text_sdk().wait(timeout=0.2):
            pass
        else:
            self.app.text_APP.click()
            self.d.swipe(0.722, 0.336, 0.722, 0.955)
            for x in xrange(3):
                if self.app.text_sdk().wait(timeout=0.2):
                    self.app.text_sdk().click()
                    break
                else:
                    self.d.swipe(0.674, 0.967,0.709, 0.428)
        self.app.btn_loading().click()
        pass

    def confirm_reset(self):
        '''改变环境，重启'''
        if self.app.img_reset().wait(timeout=2.0):
            self.d(resourceId="android:id/button1").click_exists(timeout=2.0)
        else:
            self.app.btn_loading().click_exists(timeout=1.0)  # 点击loading
        pass

    def enter_cener(self):
        '''进入用户中心'''
        self.unlock()#解锁
        self.d.app_start(self.package)#进入指定APP
        self.deal_leaks()#处理leaks
        self.deal_allows()#处理运行权限
        self.choice_env_host()#检查并设置环境、宿主
        self.confirm_reset()#若切换环境，点击确认重启,若没有则点击loading按钮
        self.app.btn_login_out().click_exists(timeout=1.0)#清除登录
        # self.app.btn_switch_h5_native().click_exists(timeout=1.0)#切换模式
        time.sleep(8)#等待插件列表更新
        self.d.swipe(0.035, 0.94, 0.977, 0.933)
        time.sleep(1)
        self.d.click(0.114, 0.933)# 点击用户中心入口
        return self.d

    def deal_sys_alert(self):
        '''进入用户中心，部分手机有权限提示'''
        if self.name == '5LM0216531002430':
            self.deal_sys_alert_mate8()
        else:
            pass
        time.sleep(1)
        pass

    def deal_sys_alert_mate8(self):
        '''华为mate进入用户中心首页，显示权限弹框'''
        time.sleep(2)
        if self.d(resourceId="com.android.packageinstaller:id/permission_message", textContains=u'需要使用您的位置权').exists:
            self.d(resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click_exists(timeout=2.0)
            self.d(resourceId="com.android.packageinstaller:id/permission_allow_button").click_exists(timeout=2.0)
            self.d(resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click_exists(timeout=2.0)
            self.d(resourceId="com.android.packageinstaller:id/permission_allow_button").click_exists(timeout=2.0)
        pass

    def deal_allows(self):
        '''进入simpleApp，部分手机有权限提示'''
        if self.name == '8b4235be':
            self.allows_mi5()
        else:
            pass
        time.sleep(1)
        pass

    def allows_mi5(self):
        if self.app.mi5_allow_text.exists:
            self.app.mi5_btn_confirm.click()