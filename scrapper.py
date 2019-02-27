import scrapy as sp
from scrapy.crawler import CrawlerProcess
from time import localtime, strftime
import csv
filename = 'booking.csv'
current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())


class tableSpider(sp.Spider):
    name='deerio_spider'
    start_urls = ['http://deer.ee/catalog/']

    def parse(self, response):
        CLASS_SELECTOR = '.col-xs-3'
        for deerio in response.css(CLASS_SELECTOR):
            NAME_SELECTOR = 'a:not(.dep) ::text'
            yield {
                current_time: deerio.css(NAME_SELECTOR).extract(),
            }

def replace():
    lis = list(csv.reader(open(filename)))[-11:]
    alis = [str(a) for a in lis]
    readFile = open(filename)
    lines = readFile.readlines()
    readFile.close()
    w = open(filename,'w')
    w.writelines([item for item in lines[:-11]])
    w.close()
    a = open(filename,'a')
    a.write("," . join(alis))
    a.write('\n')
    a.close()
def execute():
    c = CrawlerProcess({
        'USER_AGENT': 'Chrome/72.0.3626.119',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'booking.csv',
        })
    c.crawl(tableSpider)
    c.start()

execute()
replace()
