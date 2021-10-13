import base64
import threading

import requests
from lxml import etree


def fetch(page):
    # 1.分析URL规则, 第一页和第N页的区别
    url = "https://sc.chinaz.com"
    if page == 1:
        url += "/tupian/ribenmeinv.html"
    else:
        url += "/tupian/ribenmeinv_" + str(page) + ".html"
    # 2.模拟浏览器请求
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }
    # 3.发送请求
    response = requests.get(url, headers=header).content.decode("utf-8")
    # 4.将bytes转换成html对象
    html = etree.HTML(response)
    # 5.提取图片
    original_image_list = html.xpath("//div[@id='container']/div[@class='box picblock col3']/div/a/img/@src2")
    # 6.过滤图片地址
    for original_image_url in original_image_list:
        image_url = original_image_url[2:].replace("_s", "")
        image_url = "https://" + image_url
        # 7.下载图片
        data = requests.get(image_url).content
        # 将图片下载保存到电脑本地
        with open(r"C:/meinv/" + str(base64.b64encode(image_url.encode("utf-8"))) + ".jpg", "wb") as file_object:
            file_object.write(data)
            print("downloaded:" + image_url)


if __name__ == "__main__":
    pages = int(input("请输入总页数："))
    for page in range(pages):
        t = threading.Thread(target=fetch, args=(page + 1,))
        t.start()
