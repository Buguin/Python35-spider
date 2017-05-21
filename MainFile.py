# -*- codeing:utf-8 -*-
import re
from collections import deque
from DataFile.ImgSpider import *
from bs4 import BeautifulSoup
import urllib.request
import urllib
__author__ = 'Buguin'



queue = deque()
visited = set()

url = 'http://news.dbanotes.net'
proxy_url = 'http://www.xicidaili.com/nn/10'

queue.append(url)
cnt = 0

img_spider = ImgSpider()
proxy_html = img_spider.rq_rdheaders_opener(proxy_url)
# print(proxy_html.text)
picture_all_soup = BeautifulSoup(proxy_html.text, 'html.parser')
# odd_proxy = picture_all_soup.findall('div', id_='wrapper')
# odd_proxy = picture_all_soup.find('div')
odd_proxy = picture_all_soup.find('table')
# eve_proxy = picture_all_soup.findall('tr', class_='')
# print('------------------------------------------------')
# print(odd_proxy)
# table_soup = BeautifulSoup(odd_proxy, 'html.parser')
odd_proxy = picture_all_soup.find('table').find_all('tr', class_='odd')
# print('------------------------------------------------')
# print(odd_proxy)
eve_proxy = picture_all_soup.find('table').find_all('tr', class_='')
# print('------------------------------------------------')
# print(odd_proxy)
# ip_pattern = re.compile(r"((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)/(\d\d)")
ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
port_pattern = re.compile(r"\d{3,5}[^.]")
for odd_tr in odd_proxy:
    # odd_tr = '''<td>111.155.116.202</td>'''
    # print(type(odd_tr))
    # print(odd_tr.contents)
    for odd_td in odd_tr.stripped_strings:
        if ip_pattern.match(odd_td):
            print(ip_pattern.match(odd_td).group())
        if port_pattern.match(odd_td):
            print(port_pattern.match(odd_td).group())
        print(odd_td)
    # print(odd_tr.find_all(text=ip_pattern))
    # print(odd_tr.find_all(text=port_pattern))
    print('------------------------------------------------')
    # ret = ip_pattern.findall(odd_tr.text, re.I | re.M)
    # str = ret.group()
    # print(ret.group())

# odd_ip = ip_pattern.match(odd_tr.encode('utf-8'))
# print(odd_ip)
# print(eve_proxy)
# while queue:
#     url = queue.popleft()
#     visited |= {url}
#
#     print('已抓取：' + str(cnt) + '  正在抓取 <----' + url)
#     cnt += 1
#
#     try:
#         urlop = urllib.request.urlopen(url, timeout=2)
#         if 'html' not in urlop.getheader('Content-Type'):
#             continue
#         data = urlop.read().decode('utf-8')
#     except:
#         continue
#
#     linkre = re.compile(r'class="title".+?href="(.+?)"')
#     for x in linkre.findall(data):
#         if 'http' in x and x not in visited:
#             queue.append(x)
#             print('加入队列 ----> ' + x)
