# -*- codeing:utf-8 -*-
import http.cookiejar
import urllib
import gzip
import requests

__author__ = 'Buguin'


# use urllib open url
def urllib_opener(headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in headers.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


# use request open url
def request_opener(url, headers={
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
}):
    start_html = requests.get(url, headers=headers, timeout=2)
    return start_html


# save file
def save_file(data, save_path):
    f_obj = open(save_path, 'wb')  # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()


def unzip(data):
    try:
        print('正在解压。。。')
        data = gzip.decompress(data)
        print('解压完毕！')
    except:
        print('未经压缩，无需解压')
    return data


def strip_folder_name(folder_name):
    folder_name = folder_name.strip()
    folder_name = folder_name.strip('?')
    return folder_name


