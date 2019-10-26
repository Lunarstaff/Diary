# image_pro_v1.py
from selenium import webdriver
import urllib.request
from urllib.error import HTTPError
import os.path
import time


# 图集类
class Album:
    def __init__(self, ab_name, ab_link, ab_path, image_name_pre):
        self.ab_name = ab_name
        self.ab_link = ab_link
        self.ab_path = ab_path
        self.image_name_pre = image_name_pre


# 获取当前系统时间yyyymmddhhmmss_str
def get_now_time():
    lm = time.localtime()
    time_str = str(lm.tm_year) + str(lm.tm_mon) + str(lm.tm_mday) + \
                str(lm.tm_hour) + str(lm.tm_min) + str(lm.tm_sec)
    return time_str


# 从指定的url下截图片到本地保存
# urllib下载图片方法：
def image_d_urllib(url, header, path_s):
    # 组成请求
    req = urllib.request.Request(url, headers=header)

    # 判断响应状态并执行
    try:
        # 获取响应
        rep = urllib.request.urlopen(req)
        if rep.getcode() == 200:
            # 判断路径是否已存在
            if os.path.exists(path_s):
                with open(path_s + get_now_time() + ".jpg", "wb") as image_f:
                    image_f.write(rep.read())
                    print("下载【exists】【{0}】OK".format(image_f.name))
            else:
                os.mkdir(path_s)
                with open(path_s + get_now_time() + ".jpg", "wb") as image_f:
                    image_f.write(rep.read())
                    print("下载【{0}】OK".format(image_f.name))
        else:
            print("下载失败！~")
    except HTTPError:
        print("响应状态异常！")


# 获取指定数量的图集Xpath路径列表
def get_abs_xpath_list(xth, num):
    '''
    :param xth: "/html/body/div[1]/div[1]/a[{}]"
    :param num: 5 图集数量，后面应该要做成参数吧
    :return: list
    '''
    l = []
    for i in range(1, num+1):
        l.append(xth.format(i))
    # 调试输出
    print("图集的xpath列表已生成，共：{0}个图集".format(len(l)))
    return l


# 在指定的url链接页面上找到指定xpath路径的元素列表，并生成 Album类对象列表
def get_ab_obj_list(url, xth_list):
    ab_obj_list = []
    option_headless = webdriver.ChromeOptions()
    option_headless.add_argument("headless")
    driver_chrome = webdriver.Chrome(chrome_options=option_headless)
    driver_chrome.get(url)
    time.sleep(5)
    for i in xth_list:
        ab_ele = driver_chrome.find_element_by_xpath(i)
        ele_ab_name = ab_ele.find_element_by_class_name("img-responsive").get_attribute("alt")
        ele_ab_link = ab_ele.get_attribute("href")
        ele_ab_path = "./" + str(ele_ab_name) + "/"
        ele_ab_image_name_pre = str(ele_ab_name) + get_now_time()
        ab_obj_list.append(Album(ele_ab_name, ele_ab_link, ele_ab_path, ele_ab_image_name_pre))
    driver_chrome.quit()
    # 调试输出
    print("图集对象列表已生成，共：{0}个图集对象".format(len(ab_obj_list)))
    return ab_obj_list


# 下载图集对象的图片
def get_image_save(h, abo, xth2):
    '''
    :param h: 浏览器header
    :param abo: 图集类实例
    :param xth2: 图集中目标图片的xpath（含通配符）
    :return:
    '''
    # ab_obj_list = []
    option_headless = webdriver.ChromeOptions()
    option_headless.add_argument("headless")
    driver_chrome = webdriver.Chrome(chrome_options=option_headless)
    driver_chrome.get(abo.ab_link)
    time.sleep(10)
    # 图片保存路径：
    p = abo.ab_path
    # 图片元素列表：
    image_ele_list = driver_chrome.find_elements_by_xpath(xth2)
    for i in image_ele_list:
        try:
            image_i = i.find_element_by_class_name("img-responsive").get_attribute("src")
            image_d_urllib(image_i, h, p)
        except:
            print("第{}个图片未找到src".format(i.text))
            continue
        finally:
            time.sleep(1)  # 等待1s 使图片文件名尾号+1


# 主函数
if __name__ == "__main__":
    target_url = "http://www.nenmp.com/30"

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
        # "Host": "www.nenmp.com",
        # "Referer": "http://www.zhuoku.com/zhuomianbizhi/star-starcn/20191024155759(3).htm",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3865.90 "
                      "Safari/537.36",
    }

    # 图集的xpath
    abs_xpath = "/html/body/div[1]/div[1]/a[{}]"

    # 图集中图片的xpath
    image_xpath = "/html/body/div[1]/div/div[1]/div[*]"

    # 生成要采集的图集xpath列表
    abs_xpath_list = get_abs_xpath_list(abs_xpath, 2)

    # 生成图集对象列表
    ab_l = get_ab_obj_list(target_url, abs_xpath_list)

    # 下载图片
    for i in ab_l:
        print("开始下载图集{}中的图片...".format(i.ab_name))
        # get_image_save(headers, i, image_xpath)
