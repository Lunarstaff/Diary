import openpyxl

data_plate_file_f = "C:\\E-Data-File\\腾讯课堂\\Diary\\内容分类\\python-selenium\\微信预约开户数据模板.xlsx"
data_plate_file_xl = openpyxl.load_workbook(data_plate_file_f)
for i in range(1,data_plate_file_xl.worksheets[0].max_row):
    print(i)