#coding=utf-8
'''
测试登录后，手机维修卡片点击
'''

def deal(func):
    '''
    1、后置处理：回到首页，历史位置
    '''
    def inner(login_phone_repair):
        d, cf, prf = login_phone_repair
        try:
            func(login_phone_repair)
        except Exception,e:
            print e.message
        finally:
            cf.page_to_index()
    return inner


@deal
def test_order_info(login_phone_repair):
    '''查看卡片订单信息页面'''
    login_phone_repair[2].enter_order()
    assert login_phone_repair[2].pr.title_order.wait(timeout=2.0)

@deal
def test_all_order(login_phone_repair):
    '''查看所有订单页面'''
    login_phone_repair[2].enter_all_order()
    assert login_phone_repair[2].pr.text_phone.wait(timeout=2.0)

@deal
def test_repair_page(login_phone_repair):
    '''查看维修预约页面'''
    login_phone_repair[2].enter_repair_appointment()
    assert login_phone_repair[2].pr.text_repair_appointment.wait(timeout=2.0)



