# image_download.py

import urllib.request
from urllib.error import HTTPError
import time


# 目标图片链接
target_image1 = "http://bizhi.zhuoku.com/wall/jie/20070409/huoying/014.jpg"
target_image2 = "http://nen.mnihao.com/up/nenmb/img/180228/1802280845395a95fbb32d382/5a95fbb6a8a4a.jpg"
target_image3 = "http://bizhi.zhuoku.com/2019/10/24/jikejunyi/jikejunyi02.jpg"
# 下载路径
p = "./"


# 获取当前系统日期时间yyyymmddhhmmss_str
def get_now_time():
    lm = time.localtime()
    time_str = str(lm.tm_year) + str(lm.tm_mon) + str(lm.tm_mday) \
               + str(lm.tm_hour) + str(lm.tm_min) + str(lm.tm_sec)
    return time_str


# 浏览器header
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;"
              "q=0.9,image/webp,image/apng,*/*;"
              "q=0.8,application/signed-exchange;"
              "v=b3",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "If-Modified-Since": "Thu, 05 Sep 2019 07:51:15 GMT",
    # "Cookie": "bdshare_firstime=1571414387023; cck_lasttime=1572056394373; cck_count=1",
    # "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    # "Host": "www.zhuoku.com",
    "Referer": "http://www.zhuoku.com/zhuomianbizhi/star-starcn/20191024155759(3).htm",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/77.0.3865.90 "
                  "Safari/537.36",
}

# urllib下载图片方法：
def image_d_urllib(url, header, path_s):
    # 组成请求
    req = urllib.request.Request(url, headers=header)

    # 判断响应状态并执行
    try:
        # 获取响应
        rep = urllib.request.urlopen(req)
        if rep.getcode() == 200:
            print("响应状态码为：{}".format(rep.getcode()))
            with open(path_s + get_now_time() + ".jpg", "wb") as image_f:
                image_f.write(rep.read())
                print("下载OK")
        else:
            print("下载失败！~")
    except HTTPError:
        print("响应状态异常！")


# requests库下载图片方法：
def image_d_requests(url, header):
    pass


# 主函数
if __name__ == "__main__":
    image_d_urllib(target_image3, headers, p)
