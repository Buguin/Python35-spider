# -*- codeing:utf-8 -*-
__author__ = 'Buguin'
import urllib.request


url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8 ')
print(data)
