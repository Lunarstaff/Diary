# json_001.py
import json
test_json = {
    'code': 200,
    'message': '成功!',
    'result':[{
        'path': 'https://news.163.com/20/0729/09/FIMP4I730001899O.html',
        'image': 'http://cms-bucket.ws.126.net/2020/0729/59675d95p00qe7k7i00ibc000s600e3c.png?imageView&thumbnail=140y88&quality=85',
        'title': '金正恩致敬中国人民志愿军 高调展示核威慑力',
        'passtime': '2020-07-30 10:00:38'
            }
        ]
   }
a = json.dumps(test_json)
print(a)
print(type(a))  # <class 'str'>
b = json.loads(a)
print(b)
print(type(b))  # <class 'dict'>
