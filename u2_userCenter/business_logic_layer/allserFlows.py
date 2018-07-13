#coding=utf-8
import time,appFlows
from presentation_layer.two_level_page import all_services
class AllserFlows(appFlows.AppFlows):
    '''全部服务页面相关业务逻辑操作'''
    def __init__(self,env,host,package):
        appFlows.AppFlows.__init__(self,env,host,package)
        self.af=all_services.AllserPage(self.d)
        pass

    def clear_services(self):
        '''清空我的服务卡'''
        time.sleep(1)
        # 找到我的服务卡父级框 子元素个数
        e = self.d(className='android.widget.ListView')[0]
        i = e.info.get('childCount')
        if i > 0:
            for x in xrange(i):
                # 使用child()[i] 只能使用下标获取，但点击操作，只能使用child(instance=x)才能正常点击
                if e.child(className='android.view.View')[i].child(className='android.view.View')[0] \
                        .child(className='android.view.View', instance=1).exists:
                    e.child(className='android.view.View')[i].child(className='android.view.View')[0] \
                        .child(className='android.view.View', instance=1).click()
                    print "del one..:%d" % i
                else:
                    continue

    def add_services(self, names):
        '''#添加我的服务卡'''
        ls = []
        # 服务名称集合为空时，返回
        if len(names) == 0:
            return "ok"

        if len(names) > 0:
            # 遍历点击元素
            for text in names:
                if self.d(description=text).exists:
                    e = self.d(description=text).sibling(className='android.view.View', instance=1)
                    time.sleep(1)
                    e.click()
                    print "get:%s" % text
                    ls.append(text)
                else:
                    continue

        names = [x for x in names if x not in ls]

        # 若遍历一遍后，见到底部元素，返回
        if self.d(description=u'寿险体检医院').exists:
            return 'end ok'

        # 若遍历一遍后，服务名称集合不为空，表示仍有元素未找到
        if len(names) > 0:
            self.d.swipe(0.5, 0.9, 0.5, 0.1)
            print "执行1次"
            for x in names:
                print x
            print "xxxxxxxxxxxx"
            self.add_services(names)