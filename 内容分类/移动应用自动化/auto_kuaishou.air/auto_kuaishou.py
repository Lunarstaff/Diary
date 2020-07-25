# -*- encoding=utf8 -*-
__author__ = "Lunar12"

from airtest.core.api import *
from time import sleep
from random import randint

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# 启动快手
def start_apk(apk_name, apk_active):
    # 调用系统命令窗口执行命令
    os.popen('adb shell am start -n %s/%s' % (apk_name, apk_active))
    
# 跳过等操作
def skip_over():
    # 先是新安装的应用会弹出隐私协议，需要点同意
    try:
        poco("com.移动应用自动化.nebula:id/button").wait_for_appearance(15)
        poco("com.移动应用自动化.nebula:id/button").click()
    except:
        print("不是新安装的应用！")
    finally:
        try:
            poco("com.移动应用自动化.nebula:id/close").wait_for_appearance(20)
            poco("com.移动应用自动化.nebula:id/close").click()
        except:
            print("未弹出分享得红包提示框！")


# 上滑视频操作
def scroll_up():
    while True:
        sleep(randint(5, 9))
        poco("android.view.View").swipe([0.0193, -0.6574], duration=0.3)

# 主函数

# 定义apk包名和初始Active
'''
package: name='com.移动应用自动化.nebula' versionCode='198' versionName='2.2.0.198'
sdkVersion:'16'
launchable-activity: name='com.yxcorp.gifshow.HomeActivity'  label='Kwai' icon=''
'''
apk_package_name = "com.移动应用自动化.nebula"
defalu_activte = "com.yxcorp.gifshow.HomeActivity"

start_apk(apk_package_name, defalu_activte)
# skip_over()
scroll_up()
    
    
    
    
    