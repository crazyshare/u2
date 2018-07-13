#coding=utf-8
'''
测试登录后，房产大咖卡片点击
'''

def deal(func):
    '''
    1、后置处理：回到首页，历史位置
    '''
    def inner(login_house_big_shot):
        d, cf, hf = login_house_big_shot
        try:
            func(login_house_big_shot)
        except Exception,e:
            print e.message
        finally:
            cf.page_to_index()
    return inner

@deal
def test_cover_news(login_house_big_shot):
    '''点击房产大咖封面新闻'''
    login_house_big_shot[2].enter_cover_house_news()
    assert login_house_big_shot[2].ar.house_title_news.wait(timeout=5.0)

@deal
def test_more_house_news(login_house_big_shot):
    """点击房产大咖卡片--更多大咖说房按钮"""
    login_house_big_shot[2].enter_more_house_news()
    assert login_house_big_shot[2].ar.house_first_news.wait(timeout=5.0)

@deal
def test_agent1(login_house_big_shot):
    """点击房产大咖卡片--经纪人1"""
    login_house_big_shot[2].enter_agent1()
    assert login_house_big_shot[2].ar.agent_img_weixin.wait(timeout=5.0)

@deal
def test_agent1(login_house_big_shot):
    """点击房产大咖卡片--经纪人1"""
    login_house_big_shot[2].enter_agent1()
    assert login_house_big_shot[2].ar.agent_img_weixin.wait(timeout=5.0)

@deal
def test_agent2(login_house_big_shot):
    """点击房产大咖卡片--经纪人1"""
    login_house_big_shot[2].enter_agent2()
    assert login_house_big_shot[2].ar.agent_img_weixin.wait(timeout=5.0)

@deal
def test_agent3(login_house_big_shot):
    """点击房产大咖卡片--经纪人1"""
    login_house_big_shot[2].enter_agent3()
    assert login_house_big_shot[2].ar.agent_img_weixin.wait(timeout=5.0)

@deal
def test_more_agents(login_house_big_shot):
    """点击房产大咖卡片--更多经纪人"""
    login_house_big_shot[2].enter_more_agents()
    assert login_house_big_shot[2].ar.agent_text_order_by.wait(timeout=5.0)
    assert login_house_big_shot[2].ar.agent_text_phone.wait(timeout=5.0)



