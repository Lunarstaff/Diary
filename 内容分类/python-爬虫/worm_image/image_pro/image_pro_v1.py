# image_pro_v1.py
from selenium import webdriver
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
    time_str = str(lm.tm_year) + str(lm.tm_mon) + str(lm.tm_mday) \
               + str(lm.tm_hour) + str(lm.tm_min) + str(lm.tm_sec)
    return time_str


# 从指定的url下截图片到本地保存
def save_src(url, ph):
    # 图片下载方案未定，这里先不写
    pass


# 获取指定数量的图集Xpath路径列表
def get_abs_xpath_list(xth, num):
    '''
    :param xth: "/html/body/div[1]/div[1]/a[{}]"
    :param num: 5
    :return: list
    '''
    l = []
    for i in range(1, num+1):
        l.append(xth.format(i))
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
        ele_ab_path = "./" + str(ele_ab_name)
        ele_ab_image_name_pre = str(ele_ab_name) + get_now_time()
        ab_obj_list.append(Album(ele_ab_name, ele_ab_link, ele_ab_path ,ele_ab_image_name_pre))
    driver_chrome.quit()
    return ab_obj_list


# 在指定的url链接页面上，下载指定xpath路径的图片
def get_image_save(url, xth2):
    # ab_obj_list = []
    option_headless = webdriver.ChromeOptions()
    option_headless.add_argument("headless")
    driver_chrome = webdriver.Chrome(chrome_options=option_headless)
    driver_chrome.get(url)
    time.sleep(10)

    # 图片元素列表：
    image_ele_list = driver_chrome.find_elements_by_xpath(xth2)
    for i in image_ele_list:
        i = i.find_element_by_class_name("img-responsive").get_attribute("src")

    # 这里也还没写完
    pass


# 主函数
if __name__ == "__main__":
    target_url = "http://www.nenmp.com/30"
    abs_xpath = "/html/body/div[1]/div[1]/a[{}]"
    image_xpath = "/html/body/div[1]/div/div[1]/div[*]"
    abs_xpath_list = get_abs_xpath_list(abs_xpath, 2)
    ab_l = get_ab_obj_list(target_url, abs_xpath_list)

    print(ab_l[0].ab_name)
    print(ab_l[1].ab_link)