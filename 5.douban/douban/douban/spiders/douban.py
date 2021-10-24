import scrapy
from scrapy import Request

from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        for movie in response.css('div.item'):
            item = DoubanItem()
            item['movie_name'] = movie.css('div.pic a img::attr(alt)').extract()
            yield item

        # 其它页
        next_page = response.css('span.next a::attr(href)').extract_first()
        if next_page:
            print('************* next_page = ' + next_page)
            yield Request(self.start_urls[0] + next_page, callback=self.parse)
