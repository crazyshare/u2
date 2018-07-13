#coding=utf-8
class SimpleApp(object):
    '''simpleapp 页面'''
    def __init__(self, d):
        self.d=d
        pass

    def btn_loading(self):
        return self.d(text='loading')

    @staticmethod
    def option_env():
        return 0.682, 0.225

    @staticmethod
    def option_host():
        return 0.674, 0.366

    def text_stg2(self):
        return self.d(resourceId="android:id/text1", text=u"stg2")

    @property
    def text_env(self):
        return self.d(resourceId="android:id/text1", instance=0)

    def text_sdk(self):
        return self.d(resourceId="android:id/text1", text='SDK')

    @property
    def text_APP(self):
        return self.d(resourceId="android:id/text1", instance=1)

    def btn_login_out(self):
        return self.d(resourceId="com.paic.example.simpleapp:id/item_home_left_btn", text=u"宿主登出")

    def btn_switch_h5_native(self):
        return self.d(resourceId="com.paic.example.simpleapp:id/item_home_left_btn", text=u"h5/native切换")

    def img_reset(self):
        return self.d(resourceId="android:id/message", textContains=u'你改变了环境或宿主或')

    def btn_reset(self):
        return self.d(resourceId="android:id/button1")

    def title_leaks(self):
        return self.d(text=u"Leaks in com.paic.example.simpleapp")

    def btn_del_all(self):
        return self.d(resourceId="com.paic.example.simpleapp:id/leak_canary_action")

    @property
    def mi5_allow_text(self):
        return self.d(resourceId="com.lbe.security.miui:id/permission_message",\
                      textContains=u'要允许PAAnydoor2017 访问您设备上')
    @property
    def mi5_btn_confirm(self):
        return self.d(resourceId="android:id/button1", text=u'允许')