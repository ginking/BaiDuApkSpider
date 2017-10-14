# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import codecs
from scrapy.exceptions import DropItem 
from apkSpider.items import ApkSpiderItem
import json
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request

class ApkspiderPipeline(FilesPipeline):
    
    def get_media_requests(self, item, info):
        for file_url in item["file_urls"]:
            #yield Request(file_url)
            yield Request(file_url,meta={'item':item,'index':item['file_urls'].index(file_url)})
    def item_completed(self, results, item, info):
    
        file_paths = [x["path"] for ok, x in results if ok]
        if not file_paths:
            raise DropItem('download failed %s'%file_paths)
        item['file_paths'] = file_paths       
        return item
    def file_path(self,request,response=None,info=None):
        
        item=request.meta['item'] #通过上面的meta传递过来item
        index=request.meta['index'] #通过上面的index传递过来列表中当前下载图片的下标
        media_guid = item['AppName'][index]+'.apk'
        filename = u'full/%s' % (media_guid)
        return filename

class CheckPipeline(object):
    """check item, and drop the duplicate one"""
    def __init__(self):
        self.names_seen = set()

    def process_item(self, item, spider):
        if item['name']:
            if item['name'] in self.names_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.names_seen.add(item['name'])
                
                return item
        else:
            raise DropItem("Missing price in %s" % item)


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = codecs.open('./output/output.json', 'wb', 'utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print line
        self.file.write(line)
        return item
