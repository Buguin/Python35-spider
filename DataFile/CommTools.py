# -*- codeing:utf-8 -*-
from DataFile.ImgSpider import *
__author__ = 'Buguin'


def strip_folder_name(folder_name):
    folder_name = folder_name.strip()
    folder_name = folder_name.strip('?')
    return folder_name


def get_proxy_ip(proxy_url='http://www.xicidaili.com/nn/10'):
    ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    # port_pattern = re.compile(r"\d{3,5}[^.]")
    img_spider = ImgSpider()
    proxy_html = img_spider.get(proxy_url)
    print(proxy_html.text)
    proxy_soup = BeautifulSoup(proxy_html.text, 'html.parser')
    # proxy_table = proxy_soup.find('table')
    proxy_odd = proxy_soup.find('table').find_all('tr', class_='odd')
    proxy_eve = proxy_soup.find('table').find_all('tr', class_='')
    for odd_tr in proxy_odd:
        for odd_td in odd_tr.stripped_strings:
            if ip_pattern.match(odd_td):
                ip_num = ip_pattern.match(odd_td).group()
                print(ip_num)
    for eve_tr in proxy_eve:
        for eve_td in eve_tr.stripped_strings:
            if ip_pattern.match(eve_td):
                ip_num = ip_pattern.match(eve_td).group()
                print(ip_num)


