#coding=utf-8
from presentation_layer import page
class LoginPage(page.Page):
    '''登录页面'''
    def __init__(self, d):
        page.Page.__init__(self,d)
        pass

    def text_name(self):
        if self.d(resourceId="com.paic.example.simpleapp:id/comm_input_txt", instance=0).exists:
            return self.d(resourceId="com.paic.example.simpleapp:id/comm_input_txt", instance=0)#2018Q1
        elif self.d(resourceId="user-id-input").exists:
            return self.d(resourceId="user-id-input")#2017Q3

    def text_pwd(self):
        if self.d(resourceId="com.paic.example.simpleapp:id/comm_input_txt", text=u"登录密码").exists:
            return self.d(resourceId="com.paic.example.simpleapp:id/comm_input_txt", text=u"登录密码")
        elif self.d(resourceId="com.paic.example.simpleapp:id/comm_input_txt",text='').exists:
            return self.d(resourceId="com.paic.example.simpleapp:id/comm_input_txt",text='')
        elif self.d(resourceId="user-psd-input").exists:
            return self.d(resourceId="user-psd-input")

    @property
    def btn_sub(self):
        if self.d(resourceId="com.paic.example.simpleapp:id/yzt_sdk_login_login_btn").exists:
            return self.d(resourceId="com.paic.example.simpleapp:id/yzt_sdk_login_login_btn")
        elif self.d(resourceId="login-button").exists:
            return self.d(resourceId="login-button")
        return None