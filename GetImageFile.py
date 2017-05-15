# -*- codeing:utf-8 -*-
from SpiderLib import urllib_opener
import requests
from bs4 import BeautifulSoup

__author__ = 'Buguin'

url_all = 'http://www.mzitu.com/all'
headers = {
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
}
# opener = urllib_opener()
# start_html = opener.open(url_all, timeout=2)
# html_data = start_html.read()
# print(html_data.decode())
start_html = requests.get(url_all, headers=headers, timeout=2)
soup = BeautifulSoup(start_html.text, 'html.parser')
class_all = soup.find('div', class_='all')
picture_list = class_all.find_all('a')
for a_tag in picture_list:
    title = a_tag.get_text()
    href = a_tag['href']
    print(title, href)
# print(class_all)
# for li in soup:
#     print(li)
