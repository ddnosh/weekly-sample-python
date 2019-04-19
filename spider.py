import urllib.request
import re
import os
import urllib


# 获取HTML网页源码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')


# 从网页源码里面获取需要的图片地址
def getImg(html):
    reg = r'href="(.+?\.jpg)" class='
    imgre = re.compile(reg)
    imglist = imgre.findall(html)

    # 保存图片资源到本地
    path = 'D:\\testPython'
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '\\'

    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '{}{}.jpg'.format(paths, x))
        x = x + 1
    return imglist

html = getHtml("http://www.yxylife.com/line/3126")
# 打印图片保存信息
print('already download size = ', len(getImg(html)))
