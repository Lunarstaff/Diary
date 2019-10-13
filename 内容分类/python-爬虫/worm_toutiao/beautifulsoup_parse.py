# beautifulsoup_parse.py
import requests
import bs4

target_url = 'https://www.toutiao.com'

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

# 今日头条主页左侧频道列表元素
target_element_01_xpath = "/html/body/div/div[2]/div[1]/div/div"
target_element_01_attrs_dic = {"class": "channel"}


# 获取指定URL的响应
def get_target_html(url_str):
    try:
        r = requests.get(url=target_url, headers=headers)
        print("请求url:\'" + url_str + "\'成功！")
        print("响应状态码：{}".format(r.status_code))
        with open("./r.html", "w", encoding="utf-8") as f:
            f.write(r.text)
        f.close()
        return r.text
    except:
        print("请求url:\'" + url_str + "\'失败！")
        return "请求url:\'" + url_str + "\'失败！"


# 找到指定属性字典的元素bs4对象
def get_element_by_attrs(html_str, attrs_dic):
    try:
        soup = bs4.BeautifulSoup(html_str, "html_parser")
        r = soup.find_all("div", attrs=attrs_dic)
        print("get_xpath_element() 找到指定元素：" + r.name())
        return r
    except:
        print("get_xpath_element() 未找到指定元素：{0}:{1}".format(attrs_dic.keys(), attrs_dic.values()))
        return


if __name__ == "__main__":
    get_element_by_attrs(get_target_html(target_url), target_element_01_attrs_dic)
