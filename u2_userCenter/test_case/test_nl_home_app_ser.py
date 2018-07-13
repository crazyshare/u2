#coding=utf-8
'''
查看需登录卡片，未登录时跳转
暂时忽略该场景
'''
import pytest
def deal1(func):
    '''
    1、未登录
    '''
    def inner(no_login_home_app_service):
        d, cf, hf = no_login_home_app_service
        try:
            func(no_login_home_app_service)
        except Exception,e:
            print e.message
        finally:
            cf.page_to_index()
    return inner

# @pytest.mark.skip(message="skip")
@deal1
def test_clear_no_login(no_login_home_app_service):
    '''未登录，点击家电清洗'''
    no_login_home_app_service[2].enter_clear()
    assert no_login_home_app_service[2].lp.btn_sub().wait(timoput=2.0)
    pass