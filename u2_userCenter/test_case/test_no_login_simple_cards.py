#coding=utf-8
'''
测试无需登录，服务卡片点击跳转
1、仅包括无需登录，跳转后为相同页面的卡片：
'''
def deal(func):
    '''
    1、未登录
    '''
    def inner(enter_center_index):
        d, cf = enter_center_index
        try:
            func(enter_center_index)
        except Exception,e:
            print e.message
        finally:
            cf.blace_to_top()#返回到用户中心首页顶部位置
    return inner

@deal
def test_check_jyh(enter_center_index):
    '''查看聚优惠页面'''
    assert enter_center_index[1].get_by_text(u'聚优惠')#查找聚优惠卡片
    enter_center_index[1].enter_jyh()#进入聚优惠页面
    assert enter_center_index[1].jyh.btn_all().wait(timeout=0.2) and enter_center_index[1].jyh.title_jyh().wait(timeout=0.2)

@deal
def test_check_nearby(enter_center_index):
    '''查看附近页面'''
    assert enter_center_index[1].get_by_text(u'附近')#查找附近卡片
    enter_center_index[1].enter_nearby()#进入附近页面
    assert enter_center_index[1].nb.img_game.wait(timeout=10)