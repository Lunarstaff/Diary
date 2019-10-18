# toutiao_pro_v1.py
# encoding=utf-8
from selenium import webdriver
import time
import jieba
import wordcloud


# 获取当前系统时间yyyymmddhhmmss_str
def get_now_time():
    lm = time.localtime()
    time_str = str(lm.tm_yday) + str(lm.tm_mon) + str(lm.tm_mday) \
               + str(lm.tm_hour) + str(lm.tm_min) + str(lm.tm_sec)
    return time_str


# 频道类TtChannel
class TtChannel:
    def __init__(self, pd_name, pd_link):
        self.pd_name = pd_name
        self.pd_link = pd_link
        self.pd_text = ""


# 获取页面,找到频道列表并生成频道对象列表
def get_html_target(url, xth):
    option_headless = webdriver.ChromeOptions()
    option_headless.add_argument("headless")
    driver_chrome = webdriver.Chrome(chrome_options=option_headless)
    driver_chrome.get(url)
    time.sleep(5)
    channel_list_ele = driver_chrome.find_elements_by_xpath(xth)
    channel_list_obj = []
    for i in channel_list_ele:
        i_name = i.text
        i_link = i.find_element_by_tag_name("a").get_attribute("href")
        if str(i_link).startswith("https://www.toutiao.com/ch"):
            channel_list_obj.append(TtChannel(str(i_name), str(i_link)))
    driver_chrome.quit()
    return channel_list_obj


# 获取频道页面，并获取频道页面新闻栏标题
def get_page_title(pd_obj, xth):
    option_headless = webdriver.ChromeOptions()
    option_headless.add_argument("headless")
    driver_chrome = webdriver.Chrome(chrome_options=option_headless)
    driver_chrome.get(pd_obj.pd_link)
    time.sleep(10)
    news_list_ele = driver_chrome.find_elements_by_xpath(xth)
    text = pd_obj.pd_text
    for i in news_list_ele:
        text = text + str(i.text)
    driver_chrome.quit()
    return text


# jieba对文本进行分词，wordcloud生成词云图片
def get_word_image(text, path_com):
    # 词排除词集合
    exclues = {"客户端", "评论", "分钟", "小时", "分钟前", "不感兴趣", "点击", "刷新"}
    # 词列表清理
    wl = jieba.lcut(text)
    wl_clear = []
    for i in wl:
        if i in(exclues):
            pass
        else:
            wl_clear.append(i)
    # 生成词云
    wc = wordcloud.WordCloud(width=1000, font_path="msyh.ttc", height=700, background_color="white")
    # 加载一段有空格分词的文本
    wc.generate(" ".join(wl_clear))
    wc.to_file(path_com + ".png")


# 主函数
if __name__ == "__main__":
    # 目标网址
    target_url = 'https://www.toutiao.com'
    url = "https://www.toutiao.com/ch/news_tech/"
    # 目标元素XPath
    target_channel_list = "/html/body/div/div[2]/div[1]/div/div/ul/li[*]"
    target_news_list = "/html/body/div/div[4]/div[2]/div[2]/div/div/div/ul/li[*]"
    clo = get_html_target(target_url, target_channel_list)
    for i in clo:
        print(i.pd_name + "--" + i.pd_link)
        i.pd_text = i.pd_text + get_page_title(i, target_news_list)
        if i.pd_text == "":
            continue
        file_path = "./toutiao_" + i.pd_name + get_now_time()
        with open(file_path + ".txt", "wt", encoding="utf-8") as pdf:
            pdf.write(i.pd_text)
        pdf.close()
        get_word_image(i.pd_text, file_path)
