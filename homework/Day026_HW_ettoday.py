import scrapy


class Hw26EttodaySpider(scrapy.Spider):
    name = 'HW26_ettoday'
    allowed_domains = ['www.ettoday.net/news/20201004/1824032.htm']
    start_urls = ['http://www.ettoday.net/news/20201004/1824032.htm/']

    def parse(self, response):
        title = response.xpath("//title/text()").get()
        content = response.xpath('//div[@itemprop="articleBody"]//p/text()').getall()
        print(title)
        print(content)
