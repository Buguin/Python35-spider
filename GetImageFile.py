# -*- codeing:utf-8 -*-
# from SpiderLib import *
from bs4 import BeautifulSoup
from DataFile.ImgSpider import *
from DataFile.CommTools import *
import time
import os

__author__ = 'Buguin'

url_all = 'http://www.mzitu.com/all'

img_spider = ImgSpider()
start_html = img_spider.rq_rdheaders_opener(url_all)
# start_html = requests.get(url_all, headers=headers, timeout=2)
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
    picture_all_html = img_spider.rq_rdheaders_opener(href)
    # picture_all_html = requests.get(href, headers=headers, timeout=2)
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
        img_html = img_spider.rq_rdheaders_opener(page_url)
        # img_html = requests.get(page_url, headers=headers, timeout=2)
        img_soup = BeautifulSoup(img_html.text, 'html.parser')
        img_main = img_soup.find('div', class_='main-image')
        img_url = img_main.find('img')['src']
        print(img_url)
        img_name = img_url[-9:-4]
        img = img_spider.rq_rdheaders_opener(img_url)
        img_file = open(img_name + '.jpg', 'ab')
        img_file.write(img.content)  # use content to save img
        img_file.close()
