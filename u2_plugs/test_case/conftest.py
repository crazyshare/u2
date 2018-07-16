#coding=utf-8
import pytest,time
import uiautomator2 as u2

@pytest.fixture(scope="session")
def start_apps():
    '''进入simpleApp'''
    d=u2.connect()
    d.app_start("com.paic.example.simpleapp")
    if d(text=u"Leaks in com.paic.example.simpleapp").exists(timeout=2):
        d.app_start("com.paic.example.simpleapp")
        time.sleep(2)
    d(resourceId="com.android.packageinstaller:id/permission_allow_button").click_exists(timeout=2)
    d(resourceId="com.android.packageinstaller:id/permission_allow_button").click_exists(timeout=2)
    d(resourceId="com.paic.example.simpleapp:id/loading").click_exists(timeout=2)
    time.sleep(5)
    return d