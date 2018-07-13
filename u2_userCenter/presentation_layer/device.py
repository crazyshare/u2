#coding=utf-8
class Device(object):
    def __init__(self,d):
        self.d=d

    def img_mi_phone(self):
        return self.d(resourceId="com.miui.home:id/icon_title", text=u"电话")



        def clear_all_app(d):
            '''清除所有后台程序'''
            d.press('recent')
            print 'NAME：%s' % NAME
            if NAME == '8b4235be':
                clear_mi5(d)  # 米5
            elif NAME.startswith('127.0.0.1'):  # 虚拟机
                clear_v_yeshen(d)  # 夜神
            pass

        # 清除后台程序--米5
        def clear_mi5(d):
            while d(className='android.view.View').exists:
                d.swipe(0.502, 0.517, 0.502, 0.02)
                time.sleep(1)
                if d(resourceId="com.miui.home:id/icon_title", text=u"电话").exists:
                    break

        # 清除后台程序--夜色模拟器
        def clear_v_yeshen(d):
            time.sleep()
            if d(resourceId="com.android.systemui:id/recent_item", className="android.widget.RelativeLayout").exists:
                for e in d(resourceId="com.android.systemui:id/recent_item", className="android.widget.RelativeLayout"):
                    w, h = util.get_size(d);
                    x, y = e.center()
                    d.swipe(n_division(x, w), n_division(y, h), 0.01, n_division(y, h))
            pass
