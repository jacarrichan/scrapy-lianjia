# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:59:31 2017

@author: zhanglu01
"""


from spider.items import HouseItem

import scrapy
#from scrapy.spiders import CrawlSpider,Rule
#from scrapy.linkextractors import LinkExtractor
import re
from scrapy_splash import SplashRequest

class ZiroomSpider(scrapy.Spider):
    # 必须定义
    name = "ziroomShanghai"
    # 初始urls
    start_urls = [
                "http://sh.ziroom.com/z/nl/z6.html"                     ,
                "http://sh.ziroom.com/z/nl/z6-d310104.html"             ,
                "http://sh.ziroom.com/z/nl/z6-d310104.html"             ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611900103.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611900104.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611900097.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611900099.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b613000343.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611100125.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b613000344.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611100127.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611900100.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611100128.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b613000345.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611900098.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310104-b611900102.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310112.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611900064.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611900068.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611900069.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611900071.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611900067.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611100115.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611900073.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611900065.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611900070.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611100120.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611100121.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611100122.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611100118.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310112-b611100119.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310115.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900123.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000290.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000292.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000294.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000295.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900130.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000296.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900131.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000299.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000300.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900136.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000302.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000304.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900139.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900138.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900141.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000308.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000310.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900143.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000313.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000314.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611101108.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000315.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b611900148.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310115-b613000316.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310108.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310108.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310108-b611900117.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310108-b611900116.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310108-b611100430.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310108-b611900118.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310108-b613000348.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310108-b611900121.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310108-b613000349.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310114.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310114.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310114-b613000268.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310114-b613000270.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310114-b613000272.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310114-b613000273.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310114-b613000275.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310114-b613000271.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310114-b613000267.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310117.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310117.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310117-b611100449.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310117-b613000336.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310117-b613000337.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310117-b613000338.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310117-b611100452.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310117-b611100450.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310107.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b611100369.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b613000319.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b613000320.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b611100370.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b613000318.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b611100415.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b611100373.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b611100375.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b611100416.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b613000321.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b611100371.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310107-b613000322.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310110.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310110.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310110-b611900108.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310110-b611900106.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310110-b611900107.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310110-b613000346.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310110-b611900110.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310110-b611900109.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310110-b611900112.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310109.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310109.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310109-b611900028.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310109-b613000263.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310109-b611900029.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310109-b611900031.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310109-b613000264.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310109-b611900033.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310109-b611900030.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310105.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b611900013.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b611100407.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b611100408.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b611900011.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b611100410.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b611100409.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b613000350.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b611900014.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310105-b611100411.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310113.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000245.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b611100420.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000247.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b611900008.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000246.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b611900003.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000248.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b611100426.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000250.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000251.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b611900001.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000253.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000252.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310113-b613000254.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310106.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310106.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310106-b611100418.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310106-b613000289.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310106-b611100417.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310106-b611100419.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310101.html           "  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611900038.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611100441.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611900062.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b613000265.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611100456.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611900036.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611900037.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611100457.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611900063.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611900061.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611900060.html"  ,
                "http://sh.ziroom.com/z/nl/z6-d310101-b611900039.html"  ,
    ]    

#    rules = (
#        # 匹配正则表达式,处理下一页,结果加到url列表中
#        Rule(LinkExtractor(allow=(r'.*/z/nl/z[1|2|6]\.html\?p=\d+$'), deny=('login\.html'),), callback='parse_items', follow=True,),
#    )
     
    # 自定义配置
    custom_settings = {
        # item处理管道
        'ITEM_PIPELINES': {
             'spider.pipelines.DuplicatesPipeline': 1,
             'spider.pipelines.SavePipeline': 2,
        },
    }
        
    #CrawlSpider中用来处理start_urls中最初的返回的方法
#    def parse_start_url(self, response):
#        self.parse_items(response)
        
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse_detail_item(self, response):
        house_item = response.meta['house_item']
        try:
            house_item['title'] = response.xpath('/html/body/div[3]/div[2]/div[1]/h2/text()').extract()[0].strip()
        except IndexError:
            house_item['title'] = ''
        house_item['link'] = response.url
        try:
            house_item['price'] = re.sub('\D','',response.xpath('/html/body/div[3]/div[2]/div[1]/p/span[2]/span[1]/text()').extract()[0])
        except IndexError:
            house_item['price'] = ''
        try:
            house_item['area'] = re.findall("面积：[\s\S]*?(\d+(?:\.\d+)?).*㎡.*",response.xpath('/html/body/div[3]/div[2]/ul/li[1]/text()').extract()[0])[0]
        except IndexError:
            house_item['area'] = ''
        try:
            house_item['rooms'] = re.findall(".*户型： (\d+)室.*",response.xpath('/html/body/div[3]/div[2]/ul/li[3]/text()').extract()[0])[0]
        except IndexError:
            house_item['rooms'] = ''
        try:
            house_item['halls'] = re.findall(".*室(\d+)厅.*",response.xpath('/html/body/div[3]/div[2]/ul/li[3]/text()').extract()[0])[0]
        except IndexError:
            house_item['halls'] = ''
        try:
            house_item['lng'] = response.xpath('//*[@id="mapsearchText"]/@data-lng').extract()[0]
        except IndexError:
            house_item['lng'] = ''
        try:
            house_item['lat'] = response.xpath('//*[@id="mapsearchText"]/@data-lat').extract()[0]
        except IndexError:
            house_item['lat'] = ''
        try:
            house_item['direction'] = re.sub('朝向： ','',response.xpath('/html/body/div[3]/div[2]/ul/li[2]/text()').extract()[0])
        except IndexError:
            house_item['direction'] = ''
        try:
            house_item['confGen'] = re.findall(".*?(\d+\.?\d*).*",response.xpath('/html/body/div[3]/div[2]/p/a/span/text()').extract()[0])[0]
        except IndexError:
            house_item['confGen'] = ''
        try:
            house_item['confType'] = re.findall(".*?\d+\.?\d* *(.*)$",response.xpath('/html/body/div[3]/div[2]/p/a/span/text()').extract()[0])[0]
        except IndexError:
            house_item['confType'] = ''
        try:
            house_item['privateBathroom'] = '1' if response.xpath('/html/body/div[3]/div[2]/p/span[@class="toilet"]/text()').extract()[0] else '0'
        except IndexError:
            house_item['privateBathroom'] = '0'
        try:
            house_item['privateBalcony'] = '1' if response.xpath('/html/body/div[3]/div[2]/p/span[@class="balcony"]/text()').extract()[0] else '0'
        except IndexError:
            house_item['privateBalcony'] = '0'
        try:
            house_item['district'] = re.findall(".*?\[(.+?) .*",response.xpath('/html/body/div[3]/div[2]/div[1]/p/span[1]/text()').extract()[0])[0]
        except IndexError:
            house_item['district'] = ''
        return house_item

    def parse(self, response):
        #with open("test.txt",'wb') as f:
        #    f.write(response.body)
        for li in response.xpath('//*[@id="houseList"]/li'):
            if "clearfix zry" not in li.xpath('@class').extract():
                house_item = HouseItem()
                try:
                    house_item['time_unit'] = re.findall(".*\((.+)\).*",li.xpath('div[3]/p[1]/span/text()').extract()[0])[0]
                except IndexError:
                    house_item['time_unit'] = ''
                try:
                    house_item['rentType'] = li.xpath('div[2]/div/p[1]/span[4]/text()').extract()[0]
                except IndexError:
                    house_item['rentType'] = ''
                try:
                    house_item['floorLoc'] = re.findall("^(\d+)/.*",li.xpath('div[2]/div/p[1]/span[2]/text()').extract()[0])[0]
                except IndexError:
                    house_item['floorLoc'] = ''
                try:
                    house_item['floorTotal'] = re.findall(".*/(\d+).*$",li.xpath('div[2]/div/p[1]/span[2]/text()').extract()[0])[0]
                except IndexError:
                    house_item['floorTotal'] = ''
                try:
                    for span in li.xpath('div[2]/p/span[2]/span[@class="subway"]'):
                        if span.xpath('text()').extract()[0].find('暖')==1 or span.xpath('text()').extract()[0].find('空调')==1:
                            house_item['heatingType'] = span.xpath('text()').extract()[0]
                            break
                except IndexError:
                    house_item['heatingType'] = ''
                
                try:
                    house_item['nearestSubWayDist'] = re.findall(".*?(\d+)米.*",li.xpath('div[2]/div/p[2]/span/text()').extract()[0])[0]
                except IndexError:
                    house_item['nearestSubWayDist'] = ''
                try:
                    house_item['confStatus'] = '0' if li.xpath('div[1]/a/img/@src').extract()[0].find('defaultPZZ')>=0 else '1'
                except IndexError:
                    house_item['confStatus'] = ''

                detail_page_link = li.xpath('div[2]/h3/a/@href').extract()[0]
                if detail_page_link:
                    detail_page_link = detail_page_link if detail_page_link.find('sh')>=0 else 'http://www.ziroom.com'+detail_page_link
                    detail_page_link = detail_page_link if detail_page_link.find('http')>=0 else 'http:'+detail_page_link
                    request = scrapy.Request(detail_page_link, callback=self.parse_detail_item)
                    request.meta['house_item'] = house_item
                    yield request
        
        #请求下一页数据
        if "next" in response.xpath('//*[@id="page"]/a/@class').extract():
            current_page_link = response.url
            if re.match('.*/z/nl/z[1|2|6]-r\d-.+?\.html\?p=\d+$',current_page_link):
                current_page_p = int(re.findall(".*\?p=(\d+).*",current_page_link)[0]) + 1
                current_page_prefix = re.findall("^(.+\?p=).*",current_page_link)[0]
                next_page_link = current_page_prefix + str(current_page_p)
                yield SplashRequest(next_page_link, self.parse, args={'wait': 0.5})
