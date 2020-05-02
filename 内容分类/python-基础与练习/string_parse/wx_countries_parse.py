"""
文本字符串解析
查每个符合“<option value="ABW">阿鲁巴</option>”的内容，
取出每个中的 国别码 和 中文名称
"""

import re
import openpyxl

# 固定量
# <option value="ABW">阿鲁巴</option> 的正则表达式的模式
country_in_wx_html_re = r'\<option\svalue\=\"[A-Z]{3}\"\>.*?\<\/option\>'
country_in_wx = re.compile(country_in_wx_html_re)
# 国别码的正则表达式
country_code_re = re.compile(r'[A-Z]{3}')
# 国家中文名称
country_name_re = re.compile(r'\>.*?\<')

# 读取文件进行模式匹配并返回
source_file = "./wx_countries.txt"
with open(source_file, "r", encoding="utf-8") as sf:
    sf_str = sf.read()
    countries_ele_list = country_in_wx.findall(sf_str)

xl_to_write = "C:\\E-Data-File\\腾讯课堂\\Diary\\内容分类\\python-selenium\\微信预约开户数据模板.xlsx"
xl_to_write_f = openpyxl.load_workbook(xl_to_write)
# 要将国别写入文件中的位置 是sheet1的第3列
(x, y) = (4, 2)
for i in countries_ele_list:
    cdc = str(country_code_re.findall(i))
    cdn = str(country_name_re.findall(i))
    s = cdc[2:-2] + "-" + cdn[3:-3]
    xl_to_write_f.worksheets[1].cell(y, x).value = s
    y += 1
xl_to_write_f.save(xl_to_write)




