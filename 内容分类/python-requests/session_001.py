import requests
import json
url = 'https://api.apiopen.top/getWangYiNews?page=1&count=1'

session_001 = requests.session()
r = session_001.get(url)
print(session_001.headers)
print(session_001.cookies)
session_001.close()
print(r.json())
