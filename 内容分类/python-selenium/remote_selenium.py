from selenium import webdriver
import time

# 配置`desired_capabilities`
desired_caps = {}
desired_caps['platform'] = 'WINDOWS'
desired_caps['browserName'] = 'firefox'
# 根据上面的配置实例化一个Remote类
remote_firefox = webdriver.Remote('http://192.168.0.122:4444/wd/hub', desired_caps)
remote_firefox.get("https://www.baidu.com")
time.sleep(5)
remote_firefox.close()

# 配置IE浏览器
desired_ie = {}
desired_ie["platform"] = "WINDOWS"
desired_ie["browserName"] = "internet explorer"  # 这里的浏览器名称不能写错，要按照server里面的来
remote_ie = webdriver.Remote('http://192.168.0.122:4444/wd/hub', desired_caps)
remote_ie.get("https://www.bilibili.com")

