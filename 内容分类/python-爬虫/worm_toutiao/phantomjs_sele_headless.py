# phantomjs_sele.py
from selenium import webdriver
import time

target_url = 'https://www.toutiao.com'
target_element_01_xpath = "/html/body/div/div[2]/div[1]/div/div"

# 使用以下方法在运行的时候可以不打开浏览器
option_headless = webdriver.ChromeOptions()
option_headless.add_argument("headless")
driver_chrome = webdriver.Chrome(chrome_options=option_headless)
driver_chrome.get(target_url)
time.sleep(5)

print(driver_chrome.find_element_by_xpath(target_element_01_xpath).get_attribute("href"))
driver_chrome.close()
