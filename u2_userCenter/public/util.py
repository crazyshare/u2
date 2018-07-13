#coding=utf-8
import os

def get_size(d):
    '''获取设备屏幕大小'''
    return d.info.get('displayWidth'), d.info.get('displayHeight')


def get_device_name_from_usb():
    '''获取设备名称（通过usb连接）'''
    name=None
    message = os.popen('adb devices').readlines()
    if message!= None and message!='':
        name=[x.split("\t")[0] for x in message if not x.startswith("List of devices")][0]
    return name

def find_e_by_text(d,text):
    '''通过文本查询元素'''
    if d(text=text):
        return d(text=text)
    elif d(description=text):
        return d(description=text)
    else:
        return None
    pass
























