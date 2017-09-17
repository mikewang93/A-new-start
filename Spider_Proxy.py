import urllib.request
import os
import random

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')
    proxies = ['172.55.35.148:82','168.55.74.11:8998','84.35.26.86:80']
    proxy = random.choice(proxies)
    Proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(Proxy_support)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    return html[a:b]

def find_img(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg' ,a, a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=' ,b)

    return img_addrs

def save_img(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open('http:'+each)
            f.write(img)

def download(folder='Download',pages = 10):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))
    for i in range(pages):
        page_num -= i
        page_url =  url +'page-' + str(page_num) + '#comments'
        img_addrs = find_img(page_url)
        save_img(folder, img_addrs)

if __name__ == '__main__':
    download()
