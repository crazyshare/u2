#coding=utf-8
import pytest
from business_logic_layer import centerFlows,homeSerFlows,phoneRepairFlows,houseBigShotFlows

def enter_center(func):
    '''
    1、作为装饰器,被装饰函数功能可选：
        2-1登录或不登录
        2-2装饰滑动到指定元素位置
    2、内层函数返回：链接实例、用户中心页面操作实例、不确定的某子页面操作实例
    '''
    def inner(request):
        cf=centerFlows.CenterFlows('stg2','host','com.paic.example.simpleapp')
        cf.enter_cener()#进入到用户中心蓝条入口
        d = cf.enter_cener_index()  # 进入用户中心插件首页
        x=None
        try:
            x=func(cf)
        except AssertionError:
            cf.clear_all_app()
        def fin():
            cf.clear_all_app()
        request.addfinalizer(fin)
        return d, cf, x
    return inner

@pytest.fixture(scope="session")
def enter_center_index(request):
    '''未登录，进入用户中心'''
    cf=centerFlows.CenterFlows('stg2','host','com.paic.example.simpleapp')
    cf.enter_cener()
    d = cf.enter_cener_index()  # 进入用户中心插件首页
    def fin():
        cf.clear_all_app()
    request.addfinalizer(fin)
    return d, cf



'''已登录的固件'''

@pytest.fixture(scope="module")
@enter_center
def login_home_app_service(cf):
    '''登录，滑动到家电服务卡片'''
    cf.login()
    hf = homeSerFlows.HomeSerFlows(cf)
    cf.get_by_text(u'家电服务')
    return hf

@pytest.fixture(scope="module")
@enter_center
def login_phone_repair(cf):
    '''登录，滑动到手机维修卡片'''
    cf.login()
    prf = phoneRepairFlows.PhoneRepairFlows(cf)
    cf.get_by_text(u'手机维修')
    return prf

@pytest.fixture(scope="module")
@enter_center
def login_house_big_shot(cf):
    '''登录，滑动到房产大咖卡片'''
    cf.login()
    hbf = houseBigShotFlows.HouseSerFlows(cf)
    assert cf.get_by_text(u'房产大咖')
    return hbf
'''
添加更多固件
'''








@pytest.fixture(scope="module")
@enter_center
def no_login_home_app_service(cf):
    '''未登录，滑动到家电服务卡片'''
    hf = homeSerFlows.HomeSerFlows(cf)
    cf.get_by_text(cf.ci.title_home_appliance_service())
    return hf




def check_fail(fun):
    '''检查用列失败，就重新进入用户中心插件首页'''
    def inner(*args,**kwargs):
        try:
            fun(*args,**kwargs)
        except Exception:
            cf = centerFlows.CenterFlows('stg2', 'host', 'com.paic.example.simpleapp')
            cf.clear_all_app()#清除当前、所有后台应用
            cf.enter_cener_index()#从新进入用户中心插件首页，保证后续用列可以使用
    return inner
