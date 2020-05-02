'''
幻听网 http://www.ting89.com/
下载有声音小说

方案一：
    分析原页面的请求与响应报文，使用requests直接下载

    - 起始URL：http://www.ting89.com/down/?15605-0.html#down
    - 响应的下载连接在 xpath = '/html/body/div/div[1]/div[2]/a'
    - 目标url:
            http://mp3-2e.ting89.com:9090/2019/49/民间奇人录/001.mp3
            http://mp3-2e.ting89.com:9090/2019/49/民间奇人录/002.mp3

            ## re = r'(http:(\/\/)mp3-2e(\.)ting89(\.)com:9090(\/)2019(\/)49(\/)民间奇人录(\/)([\d]*?)(\.)mp3)'


    - 第一页的请求为：  ## re = r'http:\/\/www.ting89\.com\/down\/\?[\d]*?-[\d]*?\.html'
    第一集url = http://www.ting89.com/down/?15605-0.html
    第二集url = http://www.ting89.com/down/?15605-1.html
    第二页
    第303集url = http://www.ting89.com/down/?15605-302.html

    Request Headers
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: bdshare_firstime=1579450203492; ASPSESSIONIDCQABBTSC=HMIKHIKBPBFKGCFDBIEGBIJK; ASPSESSIONIDSQCCBRRB=MGLLMHCCIKHKPBONCJCHNJME; ASPSESSIONIDCSBAASRC=FIPENBMBBCEGMFBOOOJOEJEN; max_cms2_v=%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_|; max_cms4_v=%u300A%u6C11%u95F4%u5947%u4EBA%u5F55%u300B%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_|; ASPSESSIONIDQQBBATRB=EOHIPOIBNBAAGGNFKMPBCDOI; ASPSESSIONIDSQADDRRB=NJGKNOIBJGIJFPLAHMJDPBJC; ASPSESSIONIDCSAACTTD=NBHOPOIBBJIHLOKFMPLAHPOC
    Host: www.ting89.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36

    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: bdshare_firstime=1579450203492; ASPSESSIONIDCQABBTSC=HMIKHIKBPBFKGCFDBIEGBIJK; ASPSESSIONIDSQCCBRRB=MGLLMHCCIKHKPBONCJCHNJME; ASPSESSIONIDCSBAASRC=FIPENBMBBCEGMFBOOOJOEJEN; ASPSESSIONIDQQBBATRB=EOHIPOIBNBAAGGNFKMPBCDOI; ASPSESSIONIDSQADDRRB=NJGKNOIBJGIJFPLAHMJDPBJC; ASPSESSIONIDCSAACTTD=NBHOPOIBBJIHLOKFMPLAHPOC; ASPSESSIONIDQSCABSQB=GCABELNBLICLNOOMELAENPDM; max_cms2_v=%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C002%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-1.html_$_|; max_cms4_v=%u300A%u6C11%u95F4%u5947%u4EBA%u5F55%u300B%20%u7B2C002%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-1.html_$_|
    Host: www.ting89.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36

    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: bdshare_firstime=1579450203492; ASPSESSIONIDCQABBTSC=HMIKHIKBPBFKGCFDBIEGBIJK; ASPSESSIONIDSQCCBRRB=MGLLMHCCIKHKPBONCJCHNJME; ASPSESSIONIDCSBAASRC=FIPENBMBBCEGMFBOOOJOEJEN; ASPSESSIONIDQQBBATRB=EOHIPOIBNBAAGGNFKMPBCDOI; ASPSESSIONIDSQADDRRB=NJGKNOIBJGIJFPLAHMJDPBJC; ASPSESSIONIDCSAACTTD=NBHOPOIBBJIHLOKFMPLAHPOC; ASPSESSIONIDQSCABSQB=GCABELNBLICLNOOMELAENPDM; max_cms2_v=%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C002%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-1.html_$_|; max_cms4_v=%u300A%u6C11%u95F4%u5947%u4EBA%u5F55%u300B%20%u7B2C002%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-1.html_$_|; ASPSESSIONIDSSAAATRA=BNAEDBECDHPNPKOIMFLGDMPA
    Host: www.ting89.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36

方案二：
    如上述方法行不通，需要使用selenium 操作浏览器来操作。

'''

import requests
import time
import os
import re


# 字符串列表转字符串
def str_list_to_str(str_list):  # ['1', '2']
    output_str = ''
    for i in str_list:
        output_str += i
    return output_str


# 从目标url下载mp3文件
def get_mp3(url):
    dir_name_list_tmp = []
    save_path_root = "C:/"
    for char_i in url:
        if re.compile(r"[a-zA-Z:.-/\d]").match(char_i):
            continue
        else:
            dir_name_list_tmp.append(char_i)
    # 取文件名和保存路径
    if dir_name_list_tmp:
        mp3_file_name = str_list_to_str(dir_name_list_tmp) + '/'
    else:
        mp3_file_name = "作品名未取到" + '/'
    save_path = save_path_root + mp3_file_name
    # 添加try
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)
    # 开始下载
    mp3_response = requests.get(url, stream=True)
    with open(save_path + mp3_file_name[:-1] + url[-7:-4] + ".mp3", "wb") as mp3_fo:
        for chunk in mp3_response.iter_content():
            mp3_fo.write(chunk)
    print(url[-7:-4] + '成功下载！')



# 主函数
if __name__ == "__main__":
    # demo
    # test_url = "http://mp3-2e.ting89.com:9090/2019/49/民间奇人录/001.mp3"
    # get_mp3(test_url)

    # 获取url列表
    # 集数 389
    # request_url_0 = "http://www.ting89.com/down/?15605-" + i + ".html"  # i = 0,1,2 ... ,n-1 (第n集)

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "bdshare_firstime=1579450203492; ASPSESSIONIDCQABBTSC=HMIKHIKBPBFKGCFDBIEGBIJK; ASPSESSIONIDSQCCBRRB=MGLLMHCCIKHKPBONCJCHNJME; ASPSESSIONIDCSBAASRC=FIPENBMBBCEGMFBOOOJOEJEN; max_cms2_v=%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_|; max_cms4_v=%u300A%u6C11%u95F4%u5947%u4EBA%u5F55%u300B%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_|; ASPSESSIONIDQQBBATRB=EOHIPOIBNBAAGGNFKMPBCDOI; ASPSESSIONIDSQADDRRB=NJGKNOIBJGIJFPLAHMJDPBJC; ASPSESSIONIDCSAACTTD=NBHOPOIBBJIHLOKFMPLAHPOC",
        "Host": "www.ting89.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }

    # 目标url
    target_url_list = []
    for i in range(389):  # N = 389
        print("第" + str(i) + "次 url 开始")
        request_url_i = "http://www.ting89.com/down/?15605-" + str(i) + ".html"
        response_i = requests.get(request_url_i, headers=headers)
        response_i.encoding = 'GBK'  # 响应的内容以GBK编码
        # 在响应中匹配目标url
        response_i_text = response_i.text
        response_i_re = re.compile(r'(http:(\/\/)mp3-2e(\.)ting89(\.)com:9090(\/)2019(\/)([\d]*?)'
                                   r'(\/)民间奇人录(\/)([\d]*?)(\.)mp3)')
        target_url_i = response_i_re.findall(response_i_text)
        if target_url_i:
            target_url_list.append(target_url_i[0][0])
            print("第" + str(i) + "次 url 结束")
        else:
            print("第" + str(i) + "次 获取的url 为空")
        time.sleep(5)

    # 创建循环下载
    for down_i in target_url_list:
        get_mp3(down_i)
        time.sleep(5)

