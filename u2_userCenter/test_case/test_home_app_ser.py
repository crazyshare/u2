#coding=utf-8
'''
测试登录后，家电服务卡片点击
'''

def deal(func):
    '''
    1、后置处理：回到首页，历史位置
    '''
    def inner(login_home_app_service):
        d, cf, hf = login_home_app_service
        try:
            func(login_home_app_service)
        except Exception,e:
            print e.message
        finally:
            cf.page_to_index()
    return inner


@deal
def test_clear(login_home_app_service):
    '''查看家电清洗'''
    login_home_app_service[2].enter_clear()
    assert login_home_app_service[2].ar.btn_settlement.wait(timeout=2.0)

@deal
def test_fix(login_home_app_service):
    '''查看家电维修'''
    login_home_app_service[2].enter_fix()
    assert login_home_app_service[2].ar.btn_settlement.wait(timeout=2.0)

@deal
def test_install(login_home_app_service):
    '''查看家电安装'''
    login_home_app_service[2].enter_install()
    assert login_home_app_service[2].ar.btn_settlement.wait(timeout=2.0)

@deal
def test_discount(login_home_app_service):
    '''查看家电优惠'''
    login_home_app_service[2].enter_discount()
    assert login_home_app_service[2].ar.btn_get_discount.wait(timeout=2.0)

@deal
def test_more(login_home_app_service):
    '''查看更多服务'''
    login_home_app_service[2].enter_more()
    assert login_home_app_service[2].ar.btn_order.wait(timeout=2.0)



