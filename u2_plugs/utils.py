#coding=utf-8

import time
#装饰函数
def enter_simple(func):
    def inner(*args,**kwargs):
        find_plugs(*args,**kwargs)#查询插件
        func(*args,**kwargs)#用列函数，断言验证
        blace_reset()#后置处理
    return inner

def blace_reset(d):
    '''插件页面返回，并重置查询位置'''

    pass

@enter_simple
def find_plugs(d,text,stop_text):
    '''寻找插件'''
    while not d(text=stop_text).exists:
        if d(text=text).click_exists(timeout=2):
            break