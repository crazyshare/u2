#coding=utf-8
from presentation_layer import page
class MoreAppliancesService(page.Page):
    '''预约挂号相关页面'''

    def __init__(self,d):
        page.Page.__init__(self,d)
        pass

    '''
    预约挂号页面
    '''
    @property
    def text_input(self):
        return self.d(description=u"请输入医院、医生、疾病")