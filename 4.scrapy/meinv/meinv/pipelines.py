# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


class MeinvPipeline(ImagesPipeline):
    # IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def file_path(self, request, response=None, info=None):
        imagename = request.url.split('/')[-1]
        return imagename

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta={'item': item})

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        return item
