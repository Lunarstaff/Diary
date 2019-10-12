# getHtmlText.py
import requests


target_url = 'https://www.toutiao.com'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;"
              "q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "tt_webid=6746949881817204231;"
              "WEATHER_CITY=%E5%8C%97%E4%BA%AC;"
              "tasessionId=u5qul777w1570896694672;"
              "s_v_web_id=d14c73fe8a65f649dca06d4cec0b43f2;"
              "tt_webid=6746949881817204231;"
              "csrftoken=6b6595d51d9590aaea31cf6eb0b9c8a9;"
              "uuid='w:f214633e4a9a48daa29e1358917a5daf'",
    "Host": "www.toutiao.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/77.0.3865.90 "
                  "Safari/537.36",
}


if __name__ == "__main__":
    r = requests.get(url=target_url, headers=headers)
    print("响应状态码为：{}".format(r.status_code))
    print("响应的页面前1000个字符为：{}".format(r.text[:1000]))
