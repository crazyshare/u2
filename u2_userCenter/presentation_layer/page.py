#coding=utf-8
class Page(object):
    '''页面类'''
    def __init__(self, d):
        self.d=d

    @staticmethod
    def option_black():
        return 0.057,0.074