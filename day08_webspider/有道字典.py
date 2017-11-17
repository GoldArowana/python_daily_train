"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: 有道字典.py
@time: 2017/11/13 10:57
@describe:
"""

import urllib.request
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'

data = {'type': 'AUTO', 'i': 'exciting', 'doctype': 'json', 'xmlVersion': '1.8',
        'keyfrom': 'fanyi.web', 'ue': 'UTF-8', 'action': 'FY_BY_CLICKBUTTON', 'typoResult': 'true'}
data = urllib.parse.urlencode(data).encode('utf-8')  # 在这里还不能直接将data作为参数，需要进行一下数据的解析才可以
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')  # decode作用是将其他形式的编码转换成python使用的Unicode编码
target = json.loads(html)
print(target)
# print(target['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
    pass
