import requests,json
payload = {'key1':'value1','key2':'value2'}
r = requests.get('http://www.baidu.com',params=payload)
print(r.url)
print(r.text)
print(r.encoding)
print(r.status_code)