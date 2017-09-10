import urllib.request
import urllib.parse
import json

content = input("请输入你想要翻译的内容:")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://www.youdao.com/'
data = {}

data['i'] = content
data['type'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1505045566109'
data['sign'] = 'b567e9a46068a7fcc6732867890999bf'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

target = json.loads(html)
print("翻译的结果为: %s" % (target['translateResult'][0][0]['tgt']))
try:
    if target['smartResult']['entries']:
        print("扩展:%s" % (target['smartResult']['entries']))
except:
    pass
