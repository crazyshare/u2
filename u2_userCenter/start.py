#coding=utf-8
import os,pytest
cur_path = os.getcwd()

# 检查adb,初始化uiautomator2
os.system("%s\\public\\deal_u2.bat" %cur_path)

#检索目录
# check_dir='%s\\test_case'% cur_path
check_dir='%s\\test_case\\test_house_big_shot.py'% cur_path
commend = "%s"  %check_dir
print commend
pytest.main("%s" %commend)