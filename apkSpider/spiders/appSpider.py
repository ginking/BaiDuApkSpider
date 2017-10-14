# -*- coding: utf-8 -*-
import scrapy
from apkSpider.items import ApkSpiderItem
from selenium import webdriver
import time


class GoogleplaySpider(scrapy.Spider):
    name = 'BaiduApp'
    allowed_domains = ['as.baidu.com']
    start_urls = ['http://as.baidu.com/software/']

    headers = {
        "HOST": "as.baidu.com",
        "Referer": "http://as.baidu.com/software/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36"
    }
    def parse(self, response):
        
        category_urls=response.css('.cate').css('.cate-body').css('a').xpath('@href').extract()


        #for category_url in category_urls:
            #for j in range(1,9):              
                #yield scrapy.Request(url='http://as.baidu.com'+category_url+'/list_'+str(j)+'.html',callback=self.parse_detail)#爬取baiduapp所有apk文件

        #yield scrapy.Request(url='http://as.baidu.com/software/503_board_100_01/',callback=self.parse_detail)#爬取单个页面

        for category_url in category_urls:#分类爬取
            if '507' in category_url:#标签编号
                for j in range(1,9):
                    yield scrapy.Request(url='http://as.baidu.com'+category_url+'/list_'+str(j)+'.html',callback=self.parse_detail)
        
            
    def parse_detail(self,response):
        item = ApkSpiderItem()
        item["name"]=response.css('.appinfo-left').css('.name').xpath('text()').extract()
        item["AppName"]=response.css('.app-detail').css('.down-btn').css('span').xpath('@data_package').extract()
        item["version"]=response.css('.app-detail').css('.down-btn').css('span').xpath('@data_versionname').extract()
        item["size"]=response.css('.appinfo-left>.down-size>.size::text').extract()
        item['tags']=response.css('.tags').css('ul').css('li').css('a').css('.cur').xpath('text()').extract()
        item['file_urls']=response.css('.app-detail').css('.down-btn').css('span').xpath('@data_url').extract()
        yield item