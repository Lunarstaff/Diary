# 写一个request请求头的转换程序，把从浏览器上复制下来的报文头直接转换成 python requests中使用的报文头

# 从浏览器上复制下来的报文头为：
'''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Cookie: bdshare_firstime=1579450203492; ASPSESSIONIDCQABBTSC=HMIKHIKBPBFKGCFDBIEGBIJK; ASPSESSIONIDSQCCBRRB=MGLLMHCCIKHKPBONCJCHNJME; ASPSESSIONIDCSBAASRC=FIPENBMBBCEGMFBOOOJOEJEN; ASPSESSIONIDQQBBATRB=EOHIPOIBNBAAGGNFKMPBCDOI; ASPSESSIONIDSQADDRRB=NJGKNOIBJGIJFPLAHMJDPBJC; ASPSESSIONIDCSAACTTD=NBHOPOIBBJIHLOKFMPLAHPOC; ASPSESSIONIDQSCABSQB=GCABELNBLICLNOOMELAENPDM; max_cms2_v=%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C002%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-1.html_$_|; max_cms4_v=%u300A%u6C11%u95F4%u5947%u4EBA%u5F55%u300B%20%u7B2C002%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-1.html_$_|; ASPSESSIONIDSSAAATRA=BNAEDBECDHPNPKOIMFLGDMPA
Host: www.ting89.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0 Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
'''

# 需要将上面的字段都加上 ""

headers_input_str = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: bdshare_firstime=1579450203492; ASPSESSIONIDCQABBTSC=HMIKHIKBPBFKGCFDBIEGBIJK; ASPSESSIONIDSQCCBRRB=MGLLMHCCIKHKPBONCJCHNJME; ASPSESSIONIDCSBAASRC=FIPENBMBBCEGMFBOOOJOEJEN; max_cms2_v=%u6C11%u95F4%u5947%u4EBA%u5F55%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_|; max_cms4_v=%u300A%u6C11%u95F4%u5947%u4EBA%u5F55%u300B%20%u7B2C001%u96C6^http%3A//www.ting89.com/playbook/%3F15605-0-0.html_$_|; ASPSESSIONIDQQBBATRB=EOHIPOIBNBAAGGNFKMPBCDOI; ASPSESSIONIDSQADDRRB=NJGKNOIBJGIJFPLAHMJDPBJC; ASPSESSIONIDCSAACTTD=NBHOPOIBBJIHLOKFMPLAHPOC
    Host: www.ting89.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
'''

def str_list_to_str(str_list):  # ['1', '2']
    output_str = ''
    for i in str_list:
        output_str += i
    return output_str


list_tmp = []
key_str = ''
value_str = ''
headers_output = {}
for i in headers_input_str:
    if i == "\n" and not list_tmp:
        continue
    elif i == ":":
        key_str = str_list_to_str(list_tmp).lstrip(" ")
        list_tmp = []
    elif i == "\n" and list_tmp:
        value_str = str_list_to_str(list_tmp).lstrip(" ")
        list_tmp = []
    else:
        list_tmp.append(i)

    if key_str and value_str:
        headers_output[key_str] = value_str
        key_str = ''
        value_str = ''

for i in headers_output.keys():
    print("\"" + i + "\": " + "\"" + headers_output[i] + "\",")

