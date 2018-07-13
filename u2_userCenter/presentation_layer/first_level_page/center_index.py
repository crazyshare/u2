#coding=utf-8
from presentation_layer import page
class CenterIndex(page.Page):
    '''用户中心首页'''
    def __init__(self,d):
        page.Page.__init__(self,d)
        pass

    '''
    进入页面
    '''
    def btn_stg2(self):
        if not self.d(resourceId="stg2"):
            return self.d(description=u"测试用环境 (STG2)")
        return self.d(resourceId="stg2")

    '''
    顶部区域
    '''
    def text_please_login(self):
        return self.d(description=u"请登录", className="android.view.View")

    def btn_all(self):
        return self.d(description=u"全部")

    def btn_setting(self):
        return self.d(className="android.view.View", instance=11)

    def btn_sign(self):
        return self.d(className="android.view.View", instance=20)

    '''
    广告位
    '''
    def btn_buoy(self):
        return self.d(resourceId="in-95511")


    '''
    服务卡片
    '''
    '''家电服务'''
    def title_home_appliance_service(self):
        if self.d(description=u"家电服务").exists:
            return self.d(description=u"家电服务")
        elif self.d(description=u"家电服务 Heading").exists:
            return self.d(description=u"家电服务 Heading")
        else:
            return None

    def text_clear_appliance(self):
        return self.d(description=u"家电清洗")

    def text_fix_appliance(self):
        return self.d(description=u"家电维修")

    def text_install_appliance(self):
        return self.d(description=u"家电安装")

    def btn_login_order(self):
        return self.d(description=u"登录下单")

    def point_get_discount(self):
        x, y = self.d(description=u'领优惠券更多服务').center()
        return x / 2, y

    def point_get_more_service(self):
        x, y = self.d(description=u'领优惠券更多服务').center()
        w = self.d.info.get('displayWidth')
        return (w + x) / 2, y

    '''聚优惠'''
    def text_jyh(self):
        return self.d(description=u"聚优惠")

    def btn_jyh_detail(self):
        return self.d(description=u"查看详情")

    '''附近'''
    def text_nearby(self):
        return self.d(description=u"探索您身边的平安服务")

    def point_hose(self):
        return self.d(resourceId="house-tab2")

    '''手机维修'''
    @property
    def title_repair_appointment(self):
        return self.d(description=u"手机维修")

    @property
    def text_order_info(self):
        return self.d(description=u"待服务订单")

    @property
    def btn_all_order(self):
        return self.d(description=u"全部订单")

    @property
    def btn_repair_appointment(self):
        return self.d(description=u"维修预约")

    '''预约挂号'''
    @property
    def title_appointment(self):
        return self.d(description=u"预约挂号")

    @property
    def btn_make_appointment(self):
        return self.d(description=u"立即预约")

    '''登录轨迹'''
    @property
    def title_login(self):
        return self.d(description=u"登录轨迹")

    @property
    def btn_find_more(self):
        return self.d(description=u"查看更多")

    '''房产大咖'''
    def title_house_big_shot(self):
        return self.d(description=u"房产大咖")

    @property
    def banner_house(self):
        return self.d(description=u"大咖说房")

    @property
    def text_cover_news(self):
        return self.d(description=u"黑石玩儿法、凯德玩儿法——哪种更适合中国？")

    @property
    def btn_more_house(self):
        return self.d(description=u"更多大咖说房")

    @property
    def banner_agent(self):
        return self.d(description=u"找经纪人")

    @property
    def img_agent1(self):
        return self.d(description=u"上海市", instance=0)

    @property
    def img_agent2(self):
        return self.d(description=u"上海市", instance=1)

    @property
    def img_agent3(self):
        return self.d(description=u"上海市", instance=2)

    @property
    def btn_more_agents(self):
        return self.d(description=u"更多经纪人")




























