# phantomjs_sele.py
from selenium import webdriver
import time

target_url = 'https://www.toutiao.com'
target_element_01_xpath = "/html/body/div/div[2]/div[1]/div/div"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;"
              "q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/77.0.3865.90 "
                  "Safari/537.36",
}


driver_phantom = webdriver.PhantomJS(executable_path='')
driver_phantom.get(target_url)
time.sleep(5)

print(driver_phantom.find_element_by_xpath(target_element_01_xpath))
driver_phantom.close()
