::若存在adb.exe就杀掉该进程
tasklist |findstr adb.exe && taskkill /im adb.exe /f
::重启adb
adb start-server
::初始化设备端uiautomator2
python -m uiautomator2 init
