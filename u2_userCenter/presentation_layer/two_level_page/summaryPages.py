#coding=utf-8
from presentation_layer import page
class SummaryPages(page.Page):
    '''
    相关页面汇总元素
    1、页面仅包括：服务卡片点击跳转后是相同页面的页面
    '''

    def __init__(self,d):
        page.Page.__init__(self,d)
        pass

    '''
    生活缴费页面
    '''
    @property
    def text_load_fail(self):
        return self.d(resourceId="tips",description=u'加载失败！')

    '''
    全部订单页面
    '''
    @property
    def text_phone(self):
        return self.d(description=u"客服电话：4008-112-112")

    '''
    维修预约页面
    '''
    @property
    def text_repair_appointment(self):
        return self.d(description=u"维修预约")



    '''
    房产大咖相关
    '''
    '''经纪人详情页面'''
    @property
    def agent_img_weixin(self):
        return self.d(description=u"微信咨询")

    '''经纪人列表页'''
    @property
    def agent_text_order_by(self):
        return self.d(description=u"从业年限高到低")

    @property
    def agent_text_phone(self):
        return self.d(description=u"电话咨询")

    '''房产信息详情页面'''
    @property
    def house_title_news(self):
        return self.d(description=u"黑石玩儿法、凯德玩儿法——哪种更适合中国？")

    '''房产信息列表页'''
    @property
    def house_first_news(self):
        return self.d(description=u"多地首套房利率上浮 上海仍有9折优惠 2018-03-08  东地产 ")