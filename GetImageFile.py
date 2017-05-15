# -*- codeing:utf-8 -*-
from SpiderLib import urllib_opener

__author__ = 'Buguin'


url_all = 'http://www.mzitu.com/all'
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.mzitu.com',
    'DNT': '1'
}
opener = urllib_opener()
start_html = opener.open(url_all, timeout=2)
html_data = start_html.read()
print(html_data.decode())


