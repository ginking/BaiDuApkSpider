# _*_ coding: utf-8 _*_
#py 2.7该程序不可用
__author__ = 'tisturdy'
__date__ = '2017/9/22 13:42'
from scrapy.cmdline import execute
import sys
import os
#将系统当前目录设置为项目根目录
#os.path.abspath(__file__)为当前文件所在绝对路径
#os.path.dirname为文件所在目录
#H:\CodePath\spider\ArticleSpider\main.py
#H:\CodePath\spider\ArticleSpider
__file__='C:\\Users\\lenovo\\Desktop\\BDapkSpider'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#执行命令，相当于在控制台cmd输入改名了
execute(["scrapy", "crawl" , "BaiduApp"])