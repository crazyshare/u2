#coding=utf-8
import time
from presentation_layer.two_level_page import summaryPages
class HouseSerFlows():
    '''房产大咖相关操作'''
    def __init__(self, cf):
        self.cf=cf
        self.d=self.cf.d
        self.ar=summaryPages.SummaryPages(self.d)#其他相关页面实例
        pass

    def enter_cover_house_news(self):
        """点击房产大咖卡片上新闻"""
        self.cf.ci.banner_house.click()
        time.sleep(1)
        self.cf.ci.text_cover_news.click()
        time.sleep(3)
        pass

    def enter_more_house_news(self):
        """点击房产大咖卡片--更多大咖说房按钮"""
        self.cf.ci.banner_house.click()
        time.sleep(1)
        self.cf.ci.btn_more_house.click()
        time.sleep(3)
        pass

    def enter_agent1(self):
        """点击房产大咖卡片--经纪人1"""
        self.cf.ci.banner_agent.click()
        time.sleep(1)
        self.cf.ci.img_agent1.click()
        pass

    def enter_agent2(self):
        """点击房产大咖卡片--经纪人2"""
        self.cf.ci.banner_agent.click()
        time.sleep(1)
        self.cf.ci.img_agent2.click()
        pass

    def enter_agent3(self):
        """点击房产大咖卡片--经纪人3"""
        self.cf.ci.banner_agent.click()
        time.sleep(1)
        self.cf.ci.img_agent3.click()
        pass

    def enter_more_agents(self):
        """点击房产大咖卡片--更多经纪人"""
        self.cf.ci.banner_agent.click()
        time.sleep(1)
        self.cf.ci.btn_more_agents.click()
        pass