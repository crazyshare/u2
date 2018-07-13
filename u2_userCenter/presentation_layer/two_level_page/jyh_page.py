#coding=utf-8
from presentation_layer import page
class JyhPage(page.Page):
    '''聚优惠页面'''

    def __init__(self,d):
        page.Page.__init__(self,d)
        pass

    def btn_all(self):
        return self.d(description=u"全部")

    def title_jyh(self):
        return self.d(resourceId="com.paic.example.simpleapp:id/rym_title_textview",text=u'平安聚优惠')