#
from airtest.core.api import *

# 连接设备
connect_device("Android:///67da04d1")  # 同样是设备字符串

# 按键事件
keyevent("KEYCODE_HOME")

'''
Android 键码
KEYCODE_HOME	按键Home	3
'''