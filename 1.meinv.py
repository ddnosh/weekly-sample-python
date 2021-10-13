import urllib.request
import re
import os
import urllib

x = 0


def fetchImageByPage(page):
    global x
    url = "https://pic.netbian.com"
    if page == 1:
        meinvurl = url + "/4kmeinv/index.html"
    else:
        meinvurl = url + "/4kmeinv/index_" + str(page) + ".html"

    # 1.获取html源码
    requesturl = urllib.request.urlopen(meinvurl)
    requesthtml = requesturl.read().decode('gbk')
    # 2.通过正则表达式获取image的url
    reg = r'src="(.+?\.jpg)" alt='
    imgreg = re.compile(reg)
    imglist = imgreg.findall(requesthtml)
    # 3.过滤图片url
    for temp in range(len(imglist) - 1, -1, -1):
        if imglist[temp].find("qqonline") >= 0:
            imglist.pop(temp)
    # 4.设置image保存路径
    path = 'C:\\meinv'
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '\\'
    # 5.保存图片到本地
    for imgurl in imglist:
        localpath = '{}{}.jpg'.format(paths, x)
        urllib.request.urlretrieve(url + imgurl, localpath)
        print("image saved path: " + localpath)
        x = x + 1


if __name__ == "__main__":
    pages = int(input("请输入总页数："))
    for page in range(pages):
        fetchImageByPage(page + 1)
