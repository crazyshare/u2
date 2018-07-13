#coding=utf-8
from presentation_layer import page
class AllserPage(page.Page):
    '''全部服务页面'''
    def __init__(self, d):
        page.Page.__init__(self,d)
        pass

    def text_title(self):
        return self.d(description=u"全部服务")

    def btn_edit(self):
        return self.d(description=u"编辑")

    def btn_confirm(self):
        return self.d(description=u"完成")