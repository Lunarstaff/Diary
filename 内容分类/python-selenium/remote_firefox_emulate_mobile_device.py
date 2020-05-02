from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
import time
import openpyxl
wx_rul = "https://testmy.orangebank.com.cn/WeiXin/773A50B48B2286170DE9A2D3FF014EAF92D09B8C815C0E0C51741AAA2FD67D" \
             "1B96C10BD04CA2737C73F42DC5CAE1AC6383D4217E902E8DC6C0A7A92A3767427EF47ADAB1B02F2BA828AACA271C56C0E10D12" \
             "D927DE2DDF5252C27C145BF42C38A810BD7CFDC2DAB28005E17A459EA7FF2363ADB5C01BEB85C7CE809B977013162D54FA5826" \
             "A647966ADDF84F3E99B6195E18E2CE916137A91B1C1820539D9D60354C504A15D997C3386D19641DD832DB95715AFF7EA0E8B0" \
             "D77C9625EF6AE9193D42D869233E79BFC031DE443B6B8E717C8CD9B5159F19DF8544AB7EE3F13FCF_bespeakService_1_1.do"

# 给浏览器定义启动参数
firefox_start_options = webdriver.FirefoxOptions()
firefox_start_options.add_argument("mobileEmulation")
# 配置`desired_capabilities`
desired_caps = {}
desired_caps['platform'] = 'WINDOWS'
desired_caps['browserName'] = 'firefox'
desired_caps['deviceName'] = 'iPhone 6'

# 根据上面的配置实例化一个Remote类
remote_firefox = webdriver.Remote('http://192.168.0.122:4444/wd/hub', desired_caps, options=firefox_start_options)
remote_firefox.maximize_window()
remote_firefox.get("https://www.baidu.com")