import scrapy
from lxml import etree

from ..items import MeinvItem


class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["sc.chinaz.com"]
    start_urls = ['https://sc.chinaz.com/tupian/ribenmeinv.html']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_page = 1

    def parse(self, response):
        html = etree.HTML(response.body)
        original_image_list = html.xpath("//div[@id='container']/div[@class='box picblock col3']/div/a/img/@src2")
        for original_image_url in original_image_list:
            image_url = original_image_url[2:].replace("_s", "")
            image_url = "https://" + image_url
            item = MeinvItem(image_url=image_url)
            yield item

        self.current_page = self.current_page + 1

        if self.current_page <= 2:
            next_page = "https://sc.chinaz.com/tupian/ribenmeinv_" + str(self.current_page) + ".html"
            if next_page is not None:
                yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
