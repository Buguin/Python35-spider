# -*- codeing:utf-8 -*-
from SpiderLib import urllib_opener
from SpiderLib import *
import requests
from bs4 import BeautifulSoup
import time
import os

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
    # create picture folder
    title = a_tag.get_text()
    picture_path = strip_folder_name(str(title))
    picture_path = os.path.join("D:\Temp", picture_path)
    print(os.path.exists(picture_path))
    if os.path.exists(picture_path) == 0:
        os.makedirs(picture_path)
    os.chdir(picture_path)  # cd to the path, created before
    # get picture url
    href = a_tag['href']
    picture_all_html = requests.get(href, headers=headers, timeout=2)
    picture_all_soup = BeautifulSoup(picture_all_html.text, 'html.parser')
    max_span = picture_all_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    print(max_span)
    time.sleep(0.06)  # 睡眠0.06秒，服务器端设置了响应间隔
    for page in range(1, int(max_span)+1):
        time.sleep(0.06)  # 睡眠0.06秒，服务器端设置了响应间隔
        if page == 1:
            page_url = href
        else:
            page_url = href + '/' + str(page)
        print(page_url)
        img_html = requests.get(page_url, headers=headers, timeout=2)
        img_soup = BeautifulSoup(img_html.text, 'html.parser')
        img_main = img_soup.find('div', class_='main-image')
        img_url = img_main.find('img')['src']
        print(img_url)
        img_name = img_url[-9:-4]
        img = requests.get(img_url, headers=headers, timeout=2)
        img_file = open(img_name + '.jpg', 'ab')
        img_file.write(img.content)  # use content to save img
        img_file.close()

# print(class_all)
# for li in soup:
#     print(li)